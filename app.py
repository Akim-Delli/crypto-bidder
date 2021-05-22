"""Crypto Interview Assessment Module."""

import os
import logging
from statistics import mean
from typing import Dict, List

from models.coins import Coin, new_coin

from dotenv import find_dotenv, load_dotenv

from persistence import db

import crypto_api

load_dotenv(find_dotenv(raise_error_if_not_found=True))

# logging.basicConfig(filename='storage/app.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO)
bold_red = "\x1b[31;1m"
reset = "\x1b[0m"
logger_format = f"%(asctime)s [%(levelname)s] {bold_red} %(message)s {reset}"

logging.basicConfig(
    level=logging.INFO,
    format=logger_format,
    handlers=[
        logging.FileHandler("storage/app.log"),
        logging.StreamHandler()
    ]
)

# You can access the environment variables as such, and any variables from the .env file will be loaded in for you to use.
# os.getenv("DB_HOST")

def get_largest_market_cap(n: int) -> List[Dict]:
    """
    Fetch the cryptocurrencies from the coingcko API
    Return the n-largest by market capitalization
    """
    coins = crypto_api.get_coins()
    return sorted(coins,
             key=lambda x : x["market_cap"],
             reverse = True)[:n]

def bid(coin: Coin) -> bool:
    order_submitted = False
    price_history = crypto_api.get_coin_price_history(coin.coingecko_id)
    price_average = round(mean([price for _, price in price_history]), 2)
    if coin.current_price < price_average:
        order_volume = 1
        crypto_api.submit_order(coin.coingecko_id, order_volume, coin.current_price)
        order_submitted = True
    
    logging.info(f"{coin.name : <13} : 10 days Price Avg {price_average : <10} | Current Price :{coin.current_price : <10} | Bid Submitted : {order_submitted}")
        
    return order_submitted 



def start_biding():
    top_three = 3
    largest_market_cap_coins = get_largest_market_cap(top_three)

    for coin in largest_market_cap_coins:
        crypto_coin = new_coin(coin)
        db.save(crypto_coin)
        bid(crypto_coin)
    

start_biding()     