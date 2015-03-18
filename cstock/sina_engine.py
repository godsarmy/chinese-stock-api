import re
import json
import datetime

from cstock.base_engine import Engine
from cstock.model import Stock, ParserException

class SinaEngine(Engine):
    """
    Sina Engine transform stock id & parse data
    """

    __slots__ = ['_url']

    DEFAULT_BASE_URL = "http://hq.sinajs.cn/list=%s"

    def __init__(self, base_url=None):

        if base_url is None:
            self._url = self.DEFAULT_BASE_URL
        else:
            self._url = base_url

        self.shanghai_transform = lambda sid: "sh%s" % sid
        self.shenzhen_transform = lambda sid: "sz%s" % sid

    def get_url(self, stock_id):
        sina_id = self.get_sina_id(stock_id)
        return self._url % sina_id

    def get_sina_id(self, stock_id):
        """

        """
        if stock_id.startswith('0') or stock_id.startswith('3'):
            return self.shenzhen_transform(stock_id)
        
        if stock_id.startswith('6'):
            return self.shanghai_transform(stock_id)
        
        raise ParserException("Unknow stock id %s" % stock_id)

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
        return self._generate_stock(obj, stock_id)

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
            close=d.get(2, None),
            price=d.get(3, None),
            high=d.get(4, None),
            low=d.get(5, None),
            volume=d.get(8, None),
            turnover=d.get(9, None),
            date=date,
            time=time,
        )


