# system library
import unittest
from datetime import datetime

# project library
from cstock.model import Stock


class TestModel(unittest.TestCase):
    
    def test_stock(self):
        stock = Stock(
            code='000626',
            time='2015-01-01',
            price=21.5,
            open=31.5,
            close=30,
            low=12
        )
        self.assertEqual(
            stock.as_dict(),
            {'high': None, 'low': 12, 'open': 31.5, 'code': '000626',
             'price': 21.5, 'time': '2015-01-01', 'close': 30, 'date': None,
             'volume': None, 'turnover': None, 'name': None}
        )
