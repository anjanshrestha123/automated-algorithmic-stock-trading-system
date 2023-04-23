import configparser
from flask import Flask
from controller.stock_trading_controller import stock_trading_controller_blueprint

# Read App configuration from a file
config = configparser.RawConfigParser()
config.read('app.properties')

# Configure flask app
app = Flask(__name__)
app.register_blueprint(stock_trading_controller_blueprint)


def get_stock_list_file_path():
    return config.get('App', 'stock.list.file.path')


def get_traded_stock_info_list_file_path():
    return config.get('App', 'traded.stock.info.list.file.path')


def get_model_path():
    return config.get('App', 'model.path')


def get_trading_system_path():
    return config.get('App', 'trading.system.path')