from time import time
import yfinance as yf

class Stock:

    def __init__(self, symbol, requestInfo = False, time_period = '1d'):
        # symbol = TSLA, AMZN etc
        self.symbol = symbol
        stock = yf.Ticker(self.symbol)
        if (requestInfo):
            print(stock.info)
        self.__history(stock, time_period)

    def __history(self, stock, time_period):
        # time_period: 1d, 1mo, 6mo, 1y, 3y, 5y, 10y
        history_data = stock.history(time_period)
        print(history_data)

msft = Stock("MSFT",time_period='1mo',requestInfo=True)