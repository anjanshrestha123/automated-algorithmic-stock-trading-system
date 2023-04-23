from config import config
import os.path


def fetch_stock_ticker_list():
    return [stock_ticker.strip().upper() for stock_ticker in open(config.get_stock_list_file_path(), 'r').read().splitlines()]


def fetch_tradeless_stock_ticker_list():
    stock_ticker_list = fetch_stock_ticker_list()

    # Populate stock ticker list based on the traded stock info list from the file
    traded_stock_ticker_list = []
    traded_stock_info_list_file_path = config.get_traded_stock_info_list_file_path()
    if os.path.isfile(traded_stock_info_list_file_path):
        traded_stock_ticker_list = [traded_stock_info.split(' ')[1]
                                    for traded_stock_info in open(traded_stock_info_list_file_path, 'r').read().splitlines()]

    return list(set(stock_ticker_list) - set(traded_stock_ticker_list))


def update_traded_stock_to_file(stock_ticker, current_price, threshold_signal_price, take_profit_signal_price, stop_loss_price, quantity):
    with open(config.get_traded_stock_info_list_file_path(), 'a') as file:
        traded_stock_info = config.get_traded_stock_info(
            stock_ticker,
            current_price,
            threshold_signal_price,
            take_profit_signal_price,
            stop_loss_price,
            quantity
        )
        file.write('{}\n'.format(traded_stock_info))
