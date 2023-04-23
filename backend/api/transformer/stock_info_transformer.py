
def transform(stock_info_list):
    tranformed_stock_info_list = []
    for stock_info in stock_info_list:
        attributes = stock_info.split(' ')
        tranformed_stock_info_list.append({
            "stock_ticker" : attributes[0],
            "current_price" : attributes[1],
            "threshold_signal_price": attributes[2],
            "take_profit_signal_price": attributes[3],
            "stop_loss_price": attributes[4],
            "quantity": attributes[5]
        })
    return tranformed_stock_info_list