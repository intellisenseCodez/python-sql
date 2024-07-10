import mysql.connector
import logging
import handler
import schema

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if "__main__" == __name__:
    try:
        connection = mysql.connector.connect(user="root",
                                             password="your-passord",
                                             host="127.0.0.1",
                                             database='fakestore')
        if connection.is_connected():
            cursor = connection.cursor()
            logger.info("Database successfully connected")
            
        # create tables
        schema.create_product_table(conn=connection, cursor=cursor)
        schema.create_cart_table(conn=connection, cursor=cursor)
        schema.create_user_table(conn=connection, cursor=cursor)
        
        # insert product
        product_data = handler.fetch_data('products') # fetch data from API
        for product in product_data:
            flatten_dict = handler.flatten_product(prod=product) # flatten each dictionary
            schema.insert_into_product(data=flatten_dict, conn=connection, cursor=cursor) # insert into table
            
        # insert cart
        cart_data = handler.fetch_data("carts")
        for cart in cart_data:
            flatten_cart = handler.flatten_cart(cart)
            for cart in flatten_cart:
                schema.insert_into_cart(data=cart, conn=connection, cursor=cursor)
                
        # insert user
        user_data = handler.fetch_data('users')
        for user in user_data:
            flatten_user = handler.flatten_user(user)
            schema.insert_into_user(data=flatten_user, conn=connection, cursor=cursor)
    except mysql.connector.Error as err:
        logger.info("Error occured while connecting to MySQL", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logger.info("MySQL connection closed")
        