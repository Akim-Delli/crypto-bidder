<h1 style="text-align: center;"> Crypto-Currency Bidding System</h1>

![crypto-currencies](https://i.kym-cdn.com/entries/icons/original/000/024/851/crypto-cropped.jpg "crypto-currencies")

## Context

Cryptocurrencies are on the rise, and we want to get in on the action. Let's build a bot that watches the prices of certain coins and their prices, and places trades for us when they hit certain levels. 


## Instructions

`make up`

or

`make exec`

should start the bot after a short delay (to make sure that the db container is fully ready)

## Improvements

### Technical
    - display on standard output should be refreshed instead of being appended
    - make code production ready:
      - unitTests
      - refactor longer functions
      - refactor logger module
      - documentation 
    - improve API code to take into account the not 200 OK responses (404 Not Found, 400 Bad Request, etc...)

### Business
    - better buying decision instead of a 10 days average
    - build ability to sell some crypto-currencies
    - set an overall budget
    - Partially Implemented (in `config.py`):
      - ability to change the frequency of trade
      -  ability to change the number of order
      - ability to change to top N market cap crypto-currencies
