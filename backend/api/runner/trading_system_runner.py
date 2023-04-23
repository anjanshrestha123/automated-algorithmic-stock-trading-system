import os
from config import config


def run_trading_system():
    return os.system('python {trading_system_path}/run.py'.format(trading_system_path=config.get_trading_system_path()))