#    Copyright (c) 2015 Walt Chen
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0


class ParserException(Exception):
    pass


class Stock(object):
    # yesterday_close is yesterday close price
    # close is today close price

    # volume: unit of stock transacted
    # turnover: total transaction money

    __slots__ = [
        'name',
        'code',
        'date',
        'time',
        'price',
        'open',
        'close',
        'high',
        'low',
        'volume',
        'turnover',
        'yesterday_close',
        'buy1p',
        'buy1v',
        'sell1p',
        'sell1v'
    ]

    def __init__(self, **argvs):

        for (k, v) in argvs.items():
            setattr(self, k, v)

    def as_dict(self):
        result = {
            i: getattr(self, i, None)
            for i in self.__slots__
            }

        # dispose date and time because they are datetime class instance
        if result['date'] is not None:
            result['date'] = str(result['date'])

        if result['time'] is not None:
            result['time'] = str(result['time'])

        return result


__all__ = ['ParserException', 'Stock']
