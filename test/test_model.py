#    Copyright (c) 2015 Walt Chen
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0

# system library
import unittest
import datetime

# project library
from cstock.model import Stock


class TestModel(unittest.TestCase):
    
    def test_stock(self):
        stock = Stock(
            code='000626',
            time=datetime.time(3, 15, 0),
            price=21.5,
            open=31.5,
            close=30,
            low=12
        )
        self.assertEqual(
            stock.as_dict(),
            {'high': None, 'low': 12, 'open': 31.5, 'code': '000626',
             'price': 21.5, 'time': '03:15:00', 'close': 30, 'date': None,
             'volume': None, 'turnover': None, 'name': None,
             'yesterday_close': None}
        )
