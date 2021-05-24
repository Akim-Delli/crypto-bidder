import os
from typing import Dict

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

def update(coin: Coin, volume):
    connection = connect()
    with connection:
        with connection.cursor() as cursor:
            # sql = "SET @ownership = (SELECT ownership FROM cryptocurrencies);"

            sql = "UPDATE `cryptocurrencies` SET `current_price` = %s, `market_cap` = %s, `ownership` = (SELECT ownership) + %s, `spent` = (SELECT spent) + %s * %s  WHERE `symbol` = %s"
            cursor.execute(sql, (coin.current_price, coin.market_cap, volume, volume, coin.current_price, coin.symbol))

        connection.commit()


def retrieve(coin: Coin) -> Dict:
        connection = connect()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `name`, `symbol`, `current_price`, `market_cap`, `ownership`, `spent`, `portfolio_value`, `gain_loss` FROM `cryptocurrencies` WHERE `symbol`=%s"
            cursor.execute(sql, (coin.symbol,))
            result = cursor.fetchone()
            
            return result

def portfolio_value() -> Dict:

    connection = connect()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT SUM(`portfolio_value`) AS total_portfolio_value, SUM(`spent`) AS cost FROM `cryptocurrencies`"
        cursor.execute(sql, None)
        result = cursor.fetchone()
        
        return result