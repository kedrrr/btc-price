from decimal import Decimal

import requests

URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


def get_btc_price():
    result = requests.get(URL).json()
    return Decimal(result['price'])


if __name__ == '__main__':
    price = get_btc_price()
    print(price)
