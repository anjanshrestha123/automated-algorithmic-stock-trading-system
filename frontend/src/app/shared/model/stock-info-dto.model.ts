export class StockInfo {
    date_time: Date;
    stock_ticker: string;
    current_price: number;
    threshold_signal_price: number;
    take_profit_signal_price: number;
    stop_loss_price: number;
    quantity: number;
}