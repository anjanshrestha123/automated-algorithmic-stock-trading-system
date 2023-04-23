from config import config
import os
from transformer import stock_info_transformer


def fetch_stock_list():
    return [stock_ticker.strip().upper() for stock_ticker in open(config.get_stock_list_file_path(), 'r').read().splitlines()]


def update_stock_list(stock_list):
    with open(config.get_stock_list_file_path(), 'w') as file:
        for stock_ticker in stock_list:
            file.write('{}\n'.format(stock_ticker.strip().upper()))


def fetch_traded_stock_info_list():
    traded_stock_info_list = []
    file_path = config.get_traded_stock_info_list_file_path()
    file_name_pattern = file_path.split('/')[-1]
    folder_path = file_path.replace(file_name_pattern, '')

    for file in os.listdir(folder_path):
        traded_stock_info_list.extend(stock_info_transformer.transform( open(folder_path + file, 'r').read().splitlines()))

    return traded_stock_info_list
