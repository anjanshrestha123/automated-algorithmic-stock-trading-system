import yfinance as yf
import datetime as dt


def get_current_price(stock_ticker):
    data = yf.download(stock_ticker, start=dt.datetime.today() - dt.timedelta(days= 1),end=dt.datetime.today(), interval='1m')
    return round(data[-1:]['Close'].values[0], 2)

