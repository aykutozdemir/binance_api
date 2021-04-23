import json
import urllib.request

import uno
import unohelper
from com.crypto.api.binance import XCryptoBinance

class BinanceImpl(unohelper.Base, XCryptoBinance):

    def __init__(self, ctx):
        self.ctx = ctx

    def BINANCEPRICE(self, symbol):
        with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/price?symbol=" + symbol) as response:
            rawResponse = response.read()
            data = json.loads(rawResponse)
            return data['price']

    def BINANCEHIGHPRICE(self, symbol):
        with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/24hr?symbol=" + symbol) as response:
            rawResponse = response.read()
            data = json.loads(rawResponse)
            return data['highPrice']

    def BINANCELOWPRICE(self, symbol):
        with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/24hr?symbol=" + symbol) as response:
            rawResponse = response.read()
            data = json.loads(rawResponse)
            return data['lowPrice']

    def BINANCEVOLUME(self, symbol):
        with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/24hr?symbol=" + symbol) as response:
            rawResponse = response.read()
            data = json.loads(rawResponse)
            return data['volume']

    def BINANCEQUOTEVOLUME(self, symbol):
        with urllib.request.urlopen("https://api.binance.com/api/v3/ticker/24hr?symbol=" + symbol) as response:
            rawResponse = response.read()
            data = json.loads(rawResponse)
            return data['quoteVolume']

def createInstance(ctx):
    return BinanceImpl(ctx)

g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance,
    "COM.CRYPTO.API.BINANCE.PYTHON.BINANCEIMPL",
    ("com.sun.star.sheet.AddIn",)
)
