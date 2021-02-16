import backtrader as bt 

class BuyHold(bt.Strategy):


    def __init__(self):
        pass

    def next(self):
        if self.position.size == 0:
            size = int(self.broker.getcash() / self.data)
            self.buy(size = size)

