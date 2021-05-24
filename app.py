"""Crypto Interview Assessment Module."""

import os
from statistics import mean
import time
from typing import Dict, List, Tuple

from logger import logger
from models.coins import Coin, new_coin

from persistence import db

from config import VOLUME_ORDER, TRADE_FREQUENCY_IN_SEC, STARTUP_TIME, TOP_MARKET_CAP_COUNT
import crypto_api


def get_largest_market_cap(n: int) -> List[Dict]:
    """
    Fetch the cryptocurrencies from the coingcko API
    Return the n-largest by market capitalization
    """
    coins = crypto_api.get_coins()
    return sorted(coins,
             key=lambda x : x["market_cap"],
             reverse = True)[:n]

def bid(coin: Coin) -> Tuple[bool, float]:
    order_submitted = False
    price_history = crypto_api.get_coin_price_history(coin.coingecko_id)
    price_average = round(mean([price for _, price in price_history]), 2)
    if coin.current_price < price_average:
        crypto_api.submit_order(coin.coingecko_id, VOLUME_ORDER, coin.current_price)
        db.update(coin, VOLUME_ORDER)
        order_submitted = True
            
    return order_submitted, price_average 


def start_biding():
    
    largest_market_cap_coins = get_largest_market_cap(TOP_MARKET_CAP_COUNT)
    logger.header()
    for coin in largest_market_cap_coins:
        crypto_coin = new_coin(coin)
        db.save(crypto_coin)
        order_submitted, ten_days_average = bid(crypto_coin)
        result = db.retrieve(crypto_coin)
        result["order_submitted"] = order_submitted
        result["ten_days_average"] = ten_days_average
        logger.logs(result)
    
    logger.print_portfolio_value(db.portfolio_value())



def main():
    print(f"### crypto-currency bidding system will start in {STARTUP_TIME} seconds ###")
    time.sleep(STARTUP_TIME)   
    while True:
        start_biding()
        time.sleep(TRADE_FREQUENCY_IN_SEC)

main()