import os
from config import config


def run_ml_model():
    return os.system('python {model_path}/run.py'.format(model_path=config.get_model_path()))