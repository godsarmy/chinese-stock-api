
import abc

class Engine(object):

    @abc.abstractmethod
    def parse(self, data, stock_id):
        pass

    @abc.abstractmethod
    def get_url(self, stock_id):
        pass

__all__ = ['Engine']
