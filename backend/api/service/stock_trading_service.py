from util import file_util
from runner import ml_model_runner, trading_system_runner


def fetch_stock_list():
    return {
        'stock_list': file_util.fetch_stock_list()
    }


def update_stock_list(request):
    file_util.update_stock_list(request['stock_list'])
    return fetch_stock_list()


def fetch_traded_stock_info_list():
    return {
        'stock_info_list': file_util.fetch_traded_stock_info_list()
    }


def run_ml_model():
    return {
        'response': str(ml_model_runner.run_ml_model())
    }


def run_trading_system():
    return {
        'response': str(trading_system_runner.run_trading_system())
    }

