# Usage:

# msft = Stock("MSFT")
# print(msft.history('2mo'))

# msft = Stock("MSFT").history('5d')
# print(msft)
# open_dict = msft['history']['open']
# for key in open_dict:
#     time = datetime.datetime.fromtimestamp(int(key[:-3])).strftime('%Y-%m-%d')
#     print("On " + key + " opening price was $" + str("%.2f") % open_dict[key])

import yfinance as yf
import pandas as pd
import json
import datetime

class Stock:

    def __init__(self, symbol):
        # symbol = TSLA, AMZN etc
        self.symbol = symbol
        self.stock = yf.Ticker(self.symbol)

    def history(self, time_period='2d'):
        # time_period: 2d, 1mo, 6mo, 1y, 3y, 5y, 10y
        # do not pull 1d or lower as yfinance API give duplicate fields
        # and python throws "index must be unique" error
        history_data = self.stock.history(time_period)
        df = json.loads(pd.DataFrame(history_data).to_json())
        # the data we have from API has date in epoch form
        # also, we have to round the price to two decimal places
        cleansed_dict = {}
        dates_dict = {}
        for col in df:
            # open, close, high, low ... loop
            inner_date_price_cleansed_dict = {}
            for index, date in enumerate(df[col]):
                # date and price loop
                cleansed_date = datetime.datetime.fromtimestamp(int(date[:-3])).strftime('%Y-%m-%d')
                cleansed_price = str("%.2f") % df[col][date]
                inner_date_price_cleansed_dict[index] = cleansed_price
                if (col == 'Open'):
                    # we will add index as key to dates as value
                    dates_dict[index] = cleansed_date
            cleansed_dict[col.lower()] = inner_date_price_cleansed_dict
        cleansed_dict['date'] = dates_dict

        return {'history': cleansed_dict}

    def info(self):
        return {'info':self.stock.info}

    def all_data(self,time_period='1d'):
        return {**self.info(), ** self.history(time_period)}