# system library
import unittest
import datetime

# project library
from cstock.hexun_engine import HexunEngine


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.engine = HexunEngine()

    def test_get_hexun_id(self):
        hexun_id = self.engine.get_engine_id('000626')
        self.assertEqual(hexun_id, '1000626')

        hexun_id = self.engine.get_engine_id('600626')
        self.assertEqual(hexun_id, '0600626')

    def test_parse(self):
        data = '_ntes_quote_callback({"1000626":{"code": "1000626", "percent": 0.008533, "high": 51.68, "askvol3": 8300, "askvol2": 2800, "askvol5": 870, "askvol4": 22600, "price": 48.46, "open": 49.9, "bid5": 48.39, "bid4": 48.4, "bid3": 48.41, "bid2": 48.45, "bid1": 48.46, "low": 47.2, "updown": 0.41, "type": "SZ", "bidvol1": 1793, "status": 0, "bidvol3": 1000, "bidvol2": 131000, "symbol": "000626", "update": "2015/03/17 15:49:21", "bidvol5": 100, "bidvol4": 5000, "volume": 11515572, "askvol1": 14300, "ask5": 48.51, "ask4": 48.5, "ask1": 48.47, "name": "\u5982\u610f\u96c6\u56e2", "ask3": 48.49, "ask2": 48.48, "arrow": "\u2191", "time": "2015/03/17 15:49:11", "yestclose": 48.05, "turnover": 568164503.64} });'

        stock = self.engine.parse(data, 'foo_id')
        self.assertEqual(len(stock), 1)
        self.assertEqual(
            stock[0].as_dict(),
            {'code': '000626',
             'high': 51.68,
             'low': 47.2,
             'open': 49.9,
             'yesterday_close': 48.05,
             'close': None,
             'price': 48.46,
             'turnover': 568164503.64,
             'volume': 11515572,
             'name': u'\u5982\u610f\u96c6\u56e2',
             'date': '2015-03-17',
             'time': '15:49:11'}
        )
