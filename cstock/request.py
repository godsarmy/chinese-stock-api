#    Copyright (c) 2015 Walt Chen
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0

import urllib.request as http


class Requester(object):
    """ Requester class for diferent engine
    """

    __slots__ = ["_engine"]

    def __init__(self, engine):
        self._engine = engine

    def request(self, stock_id, date=None):
        """request by stock id and date

        :param stock_id:
            stock id string
        :type stock_id:
            ``str``
        :param date:
            tuple of start date and stop date
            e.g. ('2014-03-04', '2014-03-05')
        :type date:
            ``tuple``
        :returns:
            tuple of stock objects
        :rtype:
            ``tuple``
        """

        stock_url = self._engine.get_url(stock_id, date)
        print(stock_url)

        request = http.Request(stock_url)
        request.add_header('Content-Type', 'application/json')
        response = http.urlopen(request)
        data = response.read().decode('cp936')

        return self._engine.parse(data, stock_id)


__all__ = ['Requester']
