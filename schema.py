import logging
import mysql.connector

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_product_table(conn, cursor):
    try:
        query = """
                CREATE TABLE IF NOT EXISTS products(
                    id INT,
                    title VARCHAR(255),
                    price float,
                    description TEXT,
                    category VARCHAR(255),
                    image VARCHAR(255),
                    rating_rate float,
                    rating_count INT
                );
        """
        cursor.execute(query)
        conn.commit()
        logger.info("Table 'products' was successfully created")
    except mysql.connector.Error as err:
        logger.info(f"An error occurred while creating the table: {err}")
        
        

def create_user_table(conn, cursor):
    try:
        query = """
                CREATE TABLE IF NOT EXISTS users(
                    id INT,
                    email VARCHAR(255),
                    username VARCHAR(255),
                    password VARCHAR(60),
                    firstname VARCHAR(255),
                    lastname VARCHAR(255),
                    phone VARCHAR(255),
                    latitude float,
                    longitude float,
                    city VARCHAR(255),
                    street VARCHAR(255),
                    number INT,
                    zipcode VARCHAR(255)
                );
        """
        cursor.execute(query)
        conn.commit()
        logger.info("Table 'users' was successfully created")
    except mysql.connector.Error as err:
        logger.info(f"An error occurred while creating the table: {err}")
        
        
def create_cart_table(conn, cursor):
    try:
        query = """
                CREATE TABLE IF NOT EXISTS carts(
                    id INT,
                    userId INT,
                    date TEXT,
                    productId INT,
                    quantity INT
                );
        """
        cursor.execute(query)
        conn.commit()
        logger.info("Table 'carts' was successfully created")
    except mysql.connector.Error as err:
        logger.info(f"An error occurred while creating the table: {err}")
        

def insert_into_product(data, conn, cursor):
    try:
        query = """
                INSERT INTO products(id, title, price, category, description, image, rating_rate, rating_count)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (data['id'], data['title'], data['price'], data['category'], data['description'], data['image'], data['rating_rate'], data['rating_count'])
        cursor.execute(query, values)
        conn.commit()
        logger.info("Data inserted into table 'products' successfully ") 
    except mysql.connector.Error as err:
        logger.info(f"An error occurred while inserting into the table: {err}") 
        
def insert_into_cart(data, conn, cursor):
    try:
        query = """
                INSERT INTO carts(id, userId, date, productId, quantity)
                VALUES (%s, %s, %s, %s, %s);
        """
        values = (data['id'], data['userId'], data['date'], data['productId'], data['quantity'])
        cursor.execute(query, values)
        conn.commit()
        logger.info("Data inserted into table 'carts' successfully ") 
    except mysql.connector.Error as err:
        logger.info(f"An error occurred while inserting into the table: {err}") 
        

def insert_into_user(data, conn, cursor):
    try:
        query = """
                INSERT INTO users(id, firstname, lastname, email, username, password, phone, latitude, longitude, city, street, number, zipcode)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (data['id'], data['firstname'], data['lastname'], data['email'], data['username'],data['password'], data['phone'], data['latitude'], data['longitude'], data['city'], data['street'], data['number'], data['zipcode'])
        cursor.execute(query, values)
        conn.commit()
        logger.info("Data inserted into table 'users' successfully ") 
    except mysql.connector.Error as err:
        logger.info(f"An error occurred while inserting into the table: {err}") 