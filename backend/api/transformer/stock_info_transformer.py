
def transform( stock_info_list):
    tranformed_stock_info_list = []
    for stock_info in stock_info_list:
        attributes = stock_info.split(' ')
        tranformed_stock_info_list.append({
            "date_time": attributes[0],
            "stock_ticker" : attributes[1],
            "current_price" : attributes[2],
            "threshold_signal_price": attributes[3],
            "take_profit_signal_price": attributes[4],
            "stop_loss_price": attributes[5],
            "quantity": attributes[6]
        })
    return tranformed_stock_info_list