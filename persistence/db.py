import os

import pymysql.cursors

from models.coins import Coin

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(raise_error_if_not_found=True))

def connect():
    # Connect to the database
    connection = pymysql.connect(host=os.getenv("DB_HOST"),
                                user=os.getenv("DB_USER"),
                                password=os.getenv("DB_PASSWORD"),
                                database=os.getenv("DB_DATABASE"),                     
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def save(coin: Coin):
    connection = connect()
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `cryptocurrencies` (`coingecko_id`, `name`, `symbol`, `current_price`, `market_cap`) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE `current_price` = %s, `market_cap` = %s"
            cursor.execute(sql, (coin.coingecko_id, coin.name, coin.symbol, coin.current_price, coin.market_cap, coin.current_price, coin.market_cap))

        connection.commit()

def fetch(coin_symbol: str):
        connection = connect()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `name`, `symbol`, `current_price`, `market_cap` FROM `cryptocurrencies` WHERE `symbol`=%s"
            cursor.execute(sql, ('coin_symbol',))
            result = cursor.fetchone()
            print(result)