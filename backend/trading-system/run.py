from service import stock_trade_service
from util import file_util

# Runs in infinite loop until exit condition occurs
#       Exit condition:
#       1. Stock market has not open yet
#       2. All the stocks listed in the file have been traded for current day

number_of_iterations = 1
while True:
    print('\n\n ***** Starting Automated Algorithmic Trading System. Iteration Number: [{}] *****'.format(number_of_iterations))
    if stock_trade_service.is_stock_market_open():
        tradeless_stock_ticker_list = file_util.fetch_tradeless_stock_ticker_list()

        if len(tradeless_stock_ticker_list) > 0:
            stock_trade_service.trade_stock(tradeless_stock_ticker_list)
        else:
            print('All the stocks have been traded for today')
            break
    else:
        print('Stock market has not open yet')
        break
    number_of_iterations += number_of_iterations




