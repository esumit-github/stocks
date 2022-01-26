import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#print(yf.Ticker("TCS.NS").info)



tickers = ['TCS.NS', 'ONGC.NS', 'LT.NS']

infos = []

for i in tickers:
    infos.append(yf.Ticker(i).info)


fundamentals = ['dividendYield', 'marketCap', 'beta', 'forwardPE']

df = pd.DataFrame(infos)

print(df)
