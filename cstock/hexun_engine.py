#    Copyright (c) 2015 Walt Chen
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0

import re
import json
import datetime

from cstock.base_engine import Engine
from cstock.model import Stock, ParserException

class HexunEngine(Engine):
    """
    Hexun Engine transform stock id & parse data
    """

    DEFAULT_BASE_URL = "http://api.money.126.net/data/feed/%s,money.api"

    def __init__(self, base_url=None):

        super(HexunEngine, self).__init__(base_url)

        self.shanghai_transform = lambda sid: "0%s" % sid
        self.shenzhen_transform = lambda sid: "1%s" % sid
 
    def get_url(self, stock_id, date=None):
        if date is not None:
            raise ParserException("Hexun Engie does not accept date")

        return super(HexunEngine, self).get_url(stock_id)

    def parse(self, data, _stock_id):
        """parse data from hexun request

        :raise:
            exceptions if data from hexun is not well-formated
        """

        def prepare_data(data):
            """because hexun does not return a standard json,
            we need to extract the real json part
            """
            regroup = re.match(r'^_ntes_quote_callback\((.*)\)', data)

            if regroup:
                return regroup.group(1)
            else:
                raise ParserException("Unable to extact json from %s" % data)

        json_string = prepare_data(data)
        obj = json.loads(json_string)
        return (self._generate_stock(obj),)

    @staticmethod
    def _generate_stock(obj):
        """obj structure is {'1000626': {'code': ...}}
        """
        stock = obj.values()[0]        

        code = stock.get('code', None)
        if code is not None:
            # we need to remove the hexun addition market digit in stock code
            code = code[1:]

        timestr = stock.get('time', None)
        if timestr is not None:
            times = timestr.split(' ')
            date = datetime.datetime.strptime(
                times[0], '%Y/%m/%d'
            ).date()
            time = datetime.datetime.strptime(
                times[1], '%H:%M:%S'
            ).time()
        else:
            time = None
            date = None

        return Stock(
            code=code,
            name=stock.get('name', None),
            price=stock.get('price', None),
            time=time,
            date=date,
            open=stock.get('open', None),
            yesterday_close=stock.get('yestclose', None),
            low=stock.get('low', None),
            high=stock.get('high', None),
            volume=stock.get('volume', None),
            turnover=stock.get('turnover', None),
        )                

__all__ = ['HexunEngine']
