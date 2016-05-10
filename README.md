
Library to get Chinese stock price

Supported Engines:
 - Hexun API
 - Sina Finance API
 - Yahoo Finance API

Usage:
    
```
from cstock.request import Requests
from cstock.hexun_engine import HexunEngine

engine = HexunEngine()
requester = Requester(engine)

stock = requester.request('000626')
print stock.as_dict()
```
