import json
import stockRecord
import stockAPI;

class Acount:
    def __init__(self, username: str, password: str, name: str, totalInvested: float, netWorth: float, stocks: list):
        self.username = username
        self.password = password
        self.name = name
        self.totalInvested = totalInvested
        self.netWorth = netWorth
        self.stocks = stocks
    def addStock(self, symbol: str, name: str, shares: int, purchasePrice: float):
        s= stockRecord.StockRecord(symbol, name, shares, purchasePrice)
        self.stocks.append(s)
    def removeStock(self, symbol: str):
        for s in self.stocks:
            if s.symbol == symbol:
                self.stocks.remove(s)
    def updateStock(self, symbol: str, shares: int, purchasePrice: float):
        for s in self.stocks:
            if s.symbol == symbol:
    
                s.shares += shares
                #get a weighted average of the purchase price
                s.purchasePrice = (s.purchasePrice * s.shares + purchasePrice * shares) / (s.shares + shares)
                
    def updateTotalInvested(self):
        t = 0
        for s in self.stocks:
            t += s.shares * s.purchasePrice
        self.totalInvested = t
    def updateNetWorth(self):
        t = 0
        for s in self.stocks:
            stock = stockAPI.Stock(s.symbol)
            t += stock.getCurrentPrice() * s.shares
        self.netWorth = t

