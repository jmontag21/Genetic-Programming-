import math
import backtrader as bt 

#the golden cross is when the stocks short term moving average crosses above tits long-term moving average
class GoldenCross(bt.Strategy):
    params = (
        ('fast',50),
        ('slow',200),
        ('order_precentage', 0.95),
        ('ticker','SPY')
        )


    #setting slow and fast Simple moving averages for plotting
    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period = self.params.fast, plotname = '50 Day Moving Average')

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period = self.params.slow, plotname = '200 Day Moving Average')

        self.crossover = bt.indicators.CrossOver(self.fast_moving_average,self.slow_moving_average)



    #having the algorithm buy shares if the golden cross occurs and sell if it occurs in the opposite direction
    def next(self):
        if (self.position.size == 0) and (self.crossover > 0):
            investment = (self.params.order_precentage * self.broker.cash)
            
            self.size = math.floor(investment / self.data.close)
            
            #print("Bought {} shares of {} at {}".format(self.size,'SPY', self.data.close[0]) )

            self.buy(size = self.size)

        if (self.position.size > 0) and (self.crossover < 0):
            #print("Sell {} shares of {} at {}".format(self.size,'SPY', self.data.close[0]) )
            self.close()