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
                print(s.shares, shares)
                if s.shares < abs(shares) and shares < 0:
                    return False
                s.shares += shares
                #get a weighted average of the purchase price
                s.purchasePrice = ((s.purchasePrice * s.shares) + (purchasePrice * shares)) / (s.shares + shares)
                return True
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
    def getStock(self,str):
        for s in self.stocks:
            if s.symbol == str:
                return s
        
    def updateFile(self):
        filename = 'Acounts/' + self.username + '.json'
        my_dict = self.__dict__()
        with open(filename, 'w') as file:
            json.dump(my_dict, file, indent=4)
            file.close()
      
            
    def __dict__(self) -> dict:
        return {'username':self.username,'password':self.password,'name':self.name,'totalInvested':self.totalInvested,'netWorth':self.netWorth,'stocks':[s.__dict__() for s in self.stocks]}

