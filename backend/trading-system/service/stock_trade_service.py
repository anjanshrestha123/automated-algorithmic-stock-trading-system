from proxy import stock_price_ml_proxy
from proxy import yahoo_finance_proxy
from proxy import alpaca_broker_proxy
from util import file_util
from pytz import timezone
from config import config
import datetime

predicted_prices_by_stock_ticker = {}


def is_stock_market_open():
    current_date_time = datetime.datetime.now(timezone(config.get_stock_market_time_zone()))

    # 0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday
    is_weekday = current_date_time.weekday() <= 4

    # check for stock market opening and closing time
    stock_market_open_time = datetime.time(config.get_stock_market_open_hour(), config.get_stock_market_open_minute())
    stock_market_close_time = datetime.time(config.get_stock_market_close_hour(), config.get_stock_market_close_minute())
    is_stock_market_office_hour = stock_market_open_time < current_date_time.time() < stock_market_close_time

    return is_weekday and is_stock_market_office_hour


def trade_stock(tradeless_stock_ticker_list):
    for stock_ticker in tradeless_stock_ticker_list:

        # Fetching general price information
        print('Started the process to trade [{}] stock'.format(stock_ticker))
        current_price = yahoo_finance_proxy.get_current_price(stock_ticker)
        threshold_signal_price = round(current_price + ((config.get_threshold_signal_in_pct() * current_price) / 100), 2)
        take_profit_signal_price = round(current_price + ((config.get_take_profit_signal_in_pct() * current_price) / 100), 2)
        stop_loss_price = round(current_price - ((config.get_stop_loss_signal_in_pct() * current_price) / 100), 2)
        print('Current Price: [{}], Threshold Signal Price: [{}], Take Profit Signal Price: [{}], Stop Loss Price: [{}]'
              .format(current_price, threshold_signal_price, take_profit_signal_price, stop_loss_price))

        # Fetching predicted prices from ML model
        if stock_ticker in predicted_prices_by_stock_ticker:
            predicted_prices = predicted_prices_by_stock_ticker[stock_ticker]
        else:
            predicted_prices = stock_price_ml_proxy.predict_stock_price(stock_ticker, config.get_number_of_predictions())
            predicted_prices_by_stock_ticker[stock_ticker] = predicted_prices

        # Execute order if certain condition is satisfied
        if any(predicted_price >= threshold_signal_price for predicted_price in predicted_prices):
            quantity = 1  # This need to be modified to have some calculation based approach
            print('Executing bracket order for [{}] with quantity [{}]'.format(stock_ticker, quantity))
            alpaca_broker_proxy.place_bracket_order(stock_ticker, stop_loss_price, take_profit_signal_price, quantity)
            file_util.update_traded_stock_to_file(stock_ticker, current_price, threshold_signal_price, take_profit_signal_price, stop_loss_price, quantity)
        else:
            print('Predicted prices are not more than threshold signal price')



