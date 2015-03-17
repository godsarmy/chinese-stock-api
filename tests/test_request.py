# system library
import unittest
from datetime import datetime

# project library
from stock.hexun_engine import HexunEngine
from stock.request import Requester
from stock.model import Stock

class TestParser(unittest.TestCase):

    def setUp(self):
        engine = HexunEngine()
        self.requester = Requester(engine)

    def test_request(self):
        stock = self.requester.request('000626')

        self.assertEqual(stock.__class__, Stock)

 
