#    Copyright (c) 2016 Roy Liu
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0

import abc

from .model import ParserException


class Engine(object):
    """Base Engine class, must be inherited
    """

    __slots__ = ['_url']

    def __init__(self, base_url=None):
        if base_url is None:
            self._url = self.DEFAULT_BASE_URL
        else:
            self._url = base_url

    @abc.abstractmethod
    def parse(self, data, stock_id):
        """
        parse the data from service URL

        :param data:
            payload string
        :type data:
            ``str``
        :param stock_id:
            raw stock/fund id
        :type stock_id:
            ``str``
        :returns:
            tuple of Stock objects
        :rtype:
            ``tuple``
        """
        pass

    def get_url(self, stock_id, date=None):
        """
        transform stock_id date into service URL

        :param stock_id:
            stock id  
        :type stock_id:
            ``str``
        :param date:
            tuple of start date & end date, optional
            e.g. ('2014-12-13', '2014-12-15')
        :type date:
            ``tuple``
        :returns:
            service URL
        :rtype:
            ``str``
        """
        engine_id = self.get_engine_id(stock_id)
        return self._url % engine_id

    def get_engine_id(self, stock_id):
        """
        transform raw stock_id into service stock id
        we regard stock/fund starting with 0 or 3 belongs to shenzhen

        :param stock_id:
            raw stock id
        :type stock_id:
            ``str``
        :returns:
            service stock id
        :rtype:
            ``str``
        """
        if stock_id.startswith('0') or stock_id.startswith('3'):
            return self.shenzhen_transform(stock_id)

        if stock_id.startswith('6'):
            return self.shanghai_transform(stock_id)

        if stock_id.lower().startswith('sh') or stock_id.lower().startswith('sz'):
            return stock_id

        raise ParserException("Unknow stock id %s" % stock_id)


__all__ = ['Engine']
