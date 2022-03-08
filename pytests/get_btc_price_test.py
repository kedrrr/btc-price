import requests_mock
from decimal import Decimal

from main import get_btc_price, URL


def test_get_btc_price():
    with requests_mock.Mocker() as m:
        m.get(URL, json={'symbol': 'BTCUSDT', 'price': '38720.01000000'})
        price = get_btc_price()

    assert isinstance(price, Decimal)
    assert price == Decimal('38720.01')
