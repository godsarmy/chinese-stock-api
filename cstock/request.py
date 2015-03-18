
import urllib2


class Requester(object):

    __slots__ = ["_engine"]

    def __init__(self, engine):

        self._engine = engine

    def request(self, stock_id):
        
        stock_url = self._engine.get_url(stock_id)

        request = urllib2.Request(stock_url)
        request.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(request)
        data = response.read()

        return self._engine.parse(data, stock_id)

__all__ = ['Requester']
