import unittest
from decimal import Decimal
from unittest import mock

from main import get_btc_price


class TestCase(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get_btc_price(self, m):
        mock_response = mock.Mock(status_code=200)
        mock_response.json.side_effect = [
            {'symbol': 'BTCUSDT', 'price': '38720.01000000'}
        ]
        m.return_value = mock_response

        price = get_btc_price()

        self.assertIsInstance(price, Decimal)
        self.assertEqual(price, Decimal('38720.01'))


if __name__ == '__main__':
    unittest.main()
