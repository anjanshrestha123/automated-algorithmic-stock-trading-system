import configparser
import datetime

# Read App configuration from a file
config = configparser.RawConfigParser()
config.read('app.properties')


def get_model_output_path(stock_ticker):
    return config.get('App', 'model.output.path').format(stock_ticker=stock_ticker)


def get_stock_list_file_path():
    return config.get('App', 'stock.list.file.path')


def get_traded_stock_info_list_file_path():
    return config.get('App', 'traded.stock.info.list.file.path').format(datetime.datetime.now())


def get_traded_stock_info(stock_ticker, current_price, threshold_signal_price, take_profit_signal_price, stop_loss_price, quantity):
    return config.get('App', 'traded.stock.info.pattern').format(
        date_time='{:%Y-%m-%dT%H:%M:%S}'.format(datetime.datetime.now()),
        stock_ticker=stock_ticker,
        current_price=current_price,
        threshold_signal_price=threshold_signal_price,
        take_profit_signal_price=take_profit_signal_price,
        stop_loss_price=stop_loss_price,
        quantity=quantity)


def get_stock_market_time_zone():
    return config.get('App', 'stock.market.time.zone')


def get_stock_market_open_hour():
    return int(config.get('App', 'stock.market.open.hour'))


def get_stock_market_open_minute():
    return int(config.get('App', 'stock.market.open.minute'))


def get_stock_market_close_hour():
    return int(config.get('App', 'stock.market.close.hour'))


def get_stock_market_close_minute():
    return int(config.get('App', 'stock.market.close.minute'))


def get_number_of_predictions():
    return int(config.get('App', 'number.of.predictions'))


def get_threshold_signal_in_pct():
    return int(config.get('App', 'threshold.signal.in.pct'))


def get_stop_loss_signal_in_pct():
    return int(config.get('App', 'stop.loss.signal.in.pct'))


def get_take_profit_signal_in_pct():
    return int(config.get('App', 'take.profit.signal.in.pct'))


def get_alpaca_api_key():
    return config.get('Alpaca', 'alpaca.api.key')


def get_alpaca_api_secret():
    return config.get('Alpaca', 'alpaca.api.secret')
