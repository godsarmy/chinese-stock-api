#    Copyright (c) 2016 Roy Liu
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0

import re
import datetime

from cstock.base_engine import Engine
from cstock.model import Stock, ParserException


class SinaEngine(Engine):
    """
    Sina Engine transform stock id & parse data
    """

    DEFAULT_BASE_URL = "http://hq.sinajs.cn/list=%s"

    def __init__(self, base_url=None):

        super(SinaEngine, self).__init__(base_url)

        self.shanghai_transform = lambda sid: "sh%s" % sid
        self.shenzhen_transform = lambda sid: "sz%s" % sid

    def get_url(self, stock_id, date=None):
        if date is not None:
            raise ParserException("Sina Engie does not accept date")

        return super(SinaEngine, self).get_url(stock_id)

    def parse(self, data, stock_id):

        def prepare_data(data):
            """because sina does not return a standard data,
            we need to extract the real data part
            """
            regroup = re.match(r'^var.*="(.*)"', data)

            if regroup:
                return regroup.group(1)
            else:
                raise ParserException("Unable to extact json from %s" % data)

        data_string = prepare_data(data)
        obj = data_string.split(',')
        return (self._generate_stock(obj, stock_id),)

    @staticmethod
    def _generate_stock(obj, stock_id):
        d = dict(enumerate(obj))

        date = d.get(30, None)
        time = d.get(31, None)

        if date is not None:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

        if time is not None:
            time = datetime.datetime.strptime(time, '%H:%M:%S').time()

        return Stock(
            code=stock_id,
            name=d.get(0, None),
            open=d.get(1, None),
            yesterday_close=d.get(2, None),
            price=d.get(3, None),
            high=d.get(4, None),
            low=d.get(5, None),
            volume=d.get(8, None),
            turnover=d.get(9, None),
            date=date,
            time=time,
            buy1p=d.get(6, None),
            buy1v=d.get(10, None),
            sell1p=d.get(7, None),
            sell1v=d.get(20, None)
        )
