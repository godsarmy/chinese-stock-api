
class ParserException(Exception):
    pass


class Stock(object):
    
    __slots__ = [
        'code',
        'time',
        'price',
        'open',
        'high',
        'low'
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
