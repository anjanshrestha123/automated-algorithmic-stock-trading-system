import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from config.config import config

# Setting up jupyter filename to run
with open(config.get('App', 'ipynb.file.path')) as ff:
    nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')


# Generate trained model for each stock in the list
for stock_ticker in open(config.get('App', 'stock.list.file.path'), 'r').read().splitlines():
    os.environ['STOCK_TICKER'] = stock_ticker.strip().upper()

    # Run the notebook
    print('Generating trained model for ', os.environ['STOCK_TICKER'])
    ep.preprocess(nb_in)
