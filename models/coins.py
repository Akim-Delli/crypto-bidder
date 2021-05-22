from dataclasses import dataclass
from typing import Dict

@dataclass
class Coin:
    coingecko_id: str
    name: str
    symbol: str
    current_price: float
    market_cap: float

def new_coin(data: Dict) -> Coin:
    return Coin(
            coingecko_id=data['id'] , 
            name=data['name'],
            symbol=data['symbol'],
            current_price=data['current_price'],
            market_cap=data['market_cap']
            )
    



