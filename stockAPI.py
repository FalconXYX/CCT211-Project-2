#we will be using the yahoo finance api to get the stock data
# to install the package: pip install yfinance --upgrade --no-cache-dir
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import pandas as pd
from tzlocal import get_localzone

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
    def getCurrentPrice(self):
        return self.stock.info['currentPrice']
    
    def getCompanyInfo(self):
        i =self.stock.info
        profile = {
            'name': i['shortName'],
            'sector': i['sector'],
            'industry': i['industry'],
            'website': i['website'],
            'employees': i['fullTimeEmployees'],
            'description': i['longBusinessSummary'],
            'marketCap': i['marketCap'],
        }
        return profile
    def getHistoricalData(self, start_date: str, end_date: str):
        data = self.stock.history(start=start_date, end=end_date)
        return data
    def getLastHourData(self):
        timelist = []
        data = self.stock.history(period='1d', interval='1m')
        data = data[-60:]
        lasthour = data["Close"]  
        index_list = lasthour.index.tolist()
        value_list = lasthour.tolist()
        local_tz = get_localzone()
        for i in index_list:
            i = i.tz_convert(local_tz)
            timelist.append(i.strftime('%H:%M'))

        return timelist, value_list
    def getLastDayData(self):
        timelist = []
        data = self.stock.history(period='1d', interval='30m')
        lastday = data["Close"]  
        index_list = lastday.index.tolist()
        value_list = lastday.tolist()
        local_tz = get_localzone()
        for i in index_list:
            i = i.tz_convert(local_tz)
            timelist.append(i.strftime('%Y-%m-%d %H:%M'))
        return timelist, value_list

    def getLastWeekData(self):
        timelist = []
        data = self.stock.history(period='1w', interval='30m')
        lastday = data["Close"]  
        index_list = lastday.index.tolist()
        value_list = lastday.tolist()
        local_tz = get_localzone()
        for i in index_list:
            i = i.tz_convert(local_tz)
            timelist.append(i.strftime('%Y-%m-%d %H:%M'))
        return timelist, value_list
    def getLastMonthData(self):
        data = self.stock.history(period='1mo', interval='12h')
        return data
    def getLast6MonthData(self):
        data = self.stock.history(period='6mo')
        return data
    def getLastYearData(self):
        data = self.stock.history(period='1y')
        return data
    def getAllTimeData(self):
        data = self.stock.history(period='max')
        return data
c = Stock('AAPL')

print(c.getLastWeekData())

