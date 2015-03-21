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

class YahooEngine(Engine):
    """
    Yahoo Engine transform stock id & parse data

    Example to get a csv file

    http://ichart.yahoo.com/table.csv?s=002475.sz&d=7&e=23&f=2014&a=6&b=23&c=2014
    """

    DEFAULT_BASE_URL = "http://ichart.yahoo.com/table.csv?s=%s&a=%d&b=%d&c=%s&d=%d&e=%d&f=%s"

    def __init__(self, base_url=None):

        super(YahooEngine, self).__init__(base_url)

        self.shanghai_transform = lambda sid: "%s.ss" % sid
        self.shenzhen_transform = lambda sid: "%s.sz" % sid

    def get_url(self, stock_id, date=None):
        """ override of :meth:`Engine.get_url`
        """
        if date is None:
            raise ParserException("Yahoo Engine require date")

        start_date = date[0].split('-')
        end_date = date[1].split('-')

        engine_id = self.get_engine_id(stock_id)

        # month value is 0 - 11
        return self._url % (
            engine_id,
            int(start_date[1]) - 1, int(start_date[2]), start_date[0],
            int(end_date[1]) - 1, int(end_date[2]), end_date[0]
        )

    def parse(self, data, stock_id):
        lineno = 0

        stocks = []
        for line in data.splitlines():

            lineno += 1
            # first line is title
            if lineno == 1:
                continue

            values = line.split(',') 
            stocks.append(self._generate_stock(values, stock_id))

        return tuple(stocks)

    @staticmethod
    def _generate_stock(obj, stock_id):
        date = datetime.datetime.strptime(obj[0], '%Y-%m-%d').date()

        return Stock(
            code=stock_id,
            date=date,
            open=obj[1],
            high=obj[2],
            low=obj[3],
            close=obj[4],
            volume=obj[5]
        )
        


__all__ = ['YahooEngine'] 
