import stockAPI
class StockRecord:
    def __init__(self, symbol: str, name: str, shares: int, purchasePrice: float):
        self.symbol = symbol
        self.name = name
        self.shares = shares
        self.purchasePrice = purchasePrice
    def getCurrentPrice(self):
        stock = stockAPI.Stock(self.symbol)
        return stock.getCurrentPrice()
    def __dict__(self) -> dict:
        return {'symbol':self.symbol,'name':self.name,'shares':self.shares,'purchasePrice':self.purchasePrice}
        