#    Copyright (c) 2015 Walt Chen
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0

# system library
import unittest
from datetime import datetime

# project library
from cstock.hexun_engine import HexunEngine
from cstock.sina_engine import SinaEngine
from cstock.yahoo_engine import YahooEngine
from cstock.request import Requester
from cstock.model import Stock

class TestRequester(unittest.TestCase):

    def setUp(self):
        engine = HexunEngine()
        self.hexun_requester = Requester(engine)
        engine = SinaEngine()
        self.sina_requester = Requester(engine)
        engine = YahooEngine()
        self.yahoo_requester = Requester(engine)

    def test_hexun_request(self):
        stock = self.hexun_requester.request('000626')
        self.assertEqual(len(stock), 1)
        self.assertEqual(stock[0].__class__, Stock)

    def test_sina_request(self):
        stock = self.sina_requester.request('002475')
        self.assertEqual(len(stock), 1)
        self.assertEqual(stock[0].__class__, Stock)

    def test_yahoo_request(self):
        stock = self.yahoo_requester.request('002475',
                                             ('2015-03-04', '2015-03-05'))
        self.assertEqual(len(stock), 2)
        self.assertEqual(stock[0].__class__, Stock)
