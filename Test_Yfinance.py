#Import packages
import yfinance as yf

msft = yf.Ticker("TCS.NS")

# get stock info
msft.info

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

print(msft.splits)
print(msft.dividends.tail(10))
