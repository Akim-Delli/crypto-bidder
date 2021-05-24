import logging
from typing import Dict

from models.coins import Coin


format_for_stdout = logging.Formatter('%(message)s')
format_for_logfile = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')

handler_logfile = logging.FileHandler('storage/logs/app.log')
handler_logfile.setLevel(logging.INFO)
handler_logfile.setFormatter(format_for_logfile)

handler_stdout = logging.StreamHandler()
handler_stdout.setLevel(logging.INFO)
handler_stdout.setFormatter(format_for_stdout)

bold_red = "\x1b[31;1m"
reset = "\x1b[0m"
logger_format_red = f"%(asctime)s [%(levelname)s] {bold_red} %(message)s {reset}"
# logger_format_green = f"%(asctime)s [%(levelname)s] {bold_green} %(message)s {reset}"


logging.basicConfig(
    level=logging.INFO,
    handlers=[
        handler_logfile,
        handler_stdout
    ]
)

def info(message: str):
    logging.info(message)

def header():
    header = "\nCrypto-Currency Name | Symbol | Market Capitalization | Current Price  | 10 days Avg | Submitted | Ownership |     Spent     |     Value     |    Gain/Loss  |"
    header_sep = "-" * (len(header) -1)
    info(header)
    info(header_sep)
    info("")

def logs(result: Dict) -> str:
    log_message = f"{result['name'] : <20} |" \
                  f" {result['symbol'] : <6} |" \
                  f" {result['market_cap'] : >21} |" \
                  f" {result['current_price'] : >13} |" \
                  f" {result['ten_days_average'] : >12} |" \
                  f" {result['order_submitted'] !r:^9} |" \
                  f" {result['ownership'] : >9} |" \
                  f" {result['spent'] : >13} |" \
                  f" {result['portfolio_value'] : >13} |" \
                  f" {result['gain_loss'] : >13} |"\

    info(log_message)

def print_portfolio_value(result: Dict):
    def print_red(message):
        print(f"\x1b[31;7m {message}\033[00m")
    def print_green(message):
        print(f"\x1b[32;7m {message}\x1B[0m")

    gain_loss = round(result['total_portfolio_value'] - result['cost'], 2)
    print()
    message = f"TOTAL PORFOLIO VALUE : USD {round(result['total_portfolio_value'], 2)}\n GAIN/LOSS : {gain_loss}"
    if gain_loss < 0 :
        print_red(message)
    else:
        print_green(message)