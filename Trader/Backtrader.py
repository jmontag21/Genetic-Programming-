import backtrader as bt
import datetime
import pandas as pd 
import os, sys, argparse
from Strategies.GoldenCross import GoldenCross
from Strategies.BuyHold import BuyHold



print(" \n STARTING RUN 1................... GOLDEN CROSS...................................... \n")

cerebro = bt.Cerebro()

TotalInvestment = 1000

InitialInvestment2 = (.30 * TotalInvestment)

InitialInvestment1 = (.70 * TotalInvestment)


cerebro.broker.setcash(InitialInvestment1)


#Loading in CSV through pandas
spy_prices = pd.read_csv('SPY.csv',index_col = 'Date', parse_dates= True)



feed = bt.feeds.PandasData(dataname = spy_prices)

#attatching data feed to SPY.CSV file
cerebro.adddata(feed)


#Choose a strategy class from your strategies folder
cerebro.addstrategy(GoldenCross)



print(" \n Starting Initial Investment1 for Golden Cross is ${} \n  ".format(cerebro.broker.getvalue()))

cerebro.run()


print(" \n Ending Portfolio value for Investment 1 with Golden Cross is ${} \n ".format(cerebro.broker.getvalue()))

ProfitNLoss1 = (cerebro.broker.getvalue() - InitialInvestment1)

#Printing profit or loss statements
if ProfitNLoss1 >= 0:
    print(" \n Your profit for Golden Cross ${} \n".format(ProfitNLoss1))
else:
    print(" \n Your loss is ${} for Golden Cross  \n".format(ProfitNLoss1 * -1))



#Run 2

print(" \n STARTING RUN 2.........................BUY HOLD.................................... \n ")


cerebro = bt.Cerebro()


InitialInvestment2 = 200



cerebro.broker.setcash(InitialInvestment2)


#Loading in CSV through pandas
spy_prices = pd.read_csv('SPY.csv',index_col = 'Date', parse_dates= True)



feed = bt.feeds.PandasData(dataname = spy_prices)

#attatching data feed to SPY.CSV file
cerebro.adddata(feed)


#Choose a strategy class from your strategies folder
cerebro.addstrategy(BuyHold)

print(" \n Your starting Investment 2 is ${}  \n ".format(cerebro.broker.getvalue()))

cerebro.run()


print(" \n Your ending portfolio value for Buy Hold is ${} \n ".format(cerebro.broker.getvalue()))

ProfitNLoss2 = (cerebro.broker.getvalue() - InitialInvestment2)

#Printing profit or loss statements
if ProfitNLoss2 >= 0:
    print(" \n Your profit is ${} for BuyHold \n".format(ProfitNLoss2))
else:
    print(" \n Your loss is ${} for BuyHold \n".format(ProfitNLoss2 * -1))

FinalPortfolioValue = (ProfitNLoss1 + ProfitNLoss2)

print(" \n Your final portfolio value is currently ${} ".format(FinalPortfolioValue + InitialInvestment1 + InitialInvestment2))

