import requests
import logging
from exception import APIException


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

BASE_URL = "https://fakestoreapi.com"

def fetch_data(url_endpoint: str) -> list:
    try:
        response = requests.get(f"{BASE_URL}/{url_endpoint}")
        if response.status_code == 200:
            content = response.json()
        else:
            raise APIException(code=response.status_code, message="Resource not found or unavailable")
    except APIException as err:
        # logger.info(f"ERROR: {APIException(code=response.status_code, message="Resource not found or unavailable")}")
        pass
        
    return content


def flatten_product(prod: dict) -> dict:
    prod_dict = {
        'id': prod['id'],
        'title': prod['title'],
        'price': prod['price'],
        'description': prod['description'],
        'category': prod['category'],
        'image': prod['image'],
        'rating_rate': prod['rating']['rate'],
        'rating_count': prod['rating']['count']
    }
    return prod_dict


def flatten_user(user: dict) -> dict:
    user_dict = {
        'id': user['id'],
        'email': user['email'],
        'username': user['username'],
        'password': user['password'],
        'firstname': user['name']['firstname'],
        'lastname': user['name']['lastname'],
        'phone': user['phone'],
        'latitude': user['address']['geolocation']['lat'],
        'longitude': user['address']['geolocation']['long'],
        'city': user['address']['city'],
        'street': user['address']['street'],
        'number': user['address']['number'],
        'zipcode': user['address']['zipcode'],
    }
    return user_dict


def flatten_cart(cart: dict):
    for index in range(len(cart['products'])):
        cart_dict = {
            'id': cart['id'],
            'userId': cart['userId'],
            'date': cart['date'],
            'productId': cart['products'][index]['productId'],
            'quantity': cart['products'][index]['quantity']
        }
        yield cart_dict