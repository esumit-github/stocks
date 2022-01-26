import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import matplotlib as plt


aapl_df = yf.download('TCS.NS', 
                      start='2019-01-01', 
                      end='2021-06-12', 
                      progress=False,
)
aapl_df.head()


aapl_df = yf.download('TCS.NS')


ticker = yf.Ticker('TCS.NS')
aapl_df = ticker.history(period="5y")
aapl_df['Close'].plot(title="TCS's stock price")
