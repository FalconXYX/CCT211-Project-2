#we will be using the yahoo finance api to get the stock data
# to install the package: pip install yfinance --upgrade --no-cache-dir
import yfinance as yf
import pandas as pd
import numpy as np
import datetime

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
    def getCurrentPrice(self):
        return self.stock.info['currentPrice']
    def getHistory(self, start_date: str, end_date: str):
        pass
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
    
c = Stock('AAPL')
print(c.getCurrentPrice())
print(c.getCompanyInfo())
    

