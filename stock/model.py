
class ParserException(Exception):
    pass


class Stock(object):
    
    # close is yesterday close price
    # there is no today close price

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
    ]

    def __init__(self, **argvs):
        
        for (k, v) in argvs.items():
            setattr(self, k, v)

    def as_dict(self):
        return {
            i: getattr(self, i, None) 
            for i in self.__slots__
        }

__all__ = ['ParserException', 'Stock']
