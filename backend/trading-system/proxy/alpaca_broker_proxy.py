from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, OrderType, OrderClass, TimeInForce
from config import config


def create_trading_client():
    return TradingClient(config.get_alpaca_api_key(), config.get_alpaca_api_secret(), paper=True)


def place_bracket_order(stock_ticker, stop_loss_price, take_profit_price, quantity):

    # Create trading client
    trading_client = create_trading_client()

    # Create market order request
    market_order_request = MarketOrderRequest(
        symbol=stock_ticker,
        qty=quantity,
        side=OrderSide.BUY,
        type=OrderType.MARKET,
        time_in_force=TimeInForce.GTC,
        order_class=OrderClass.BRACKET,
        stop_loss={'stop_price': stop_loss_price},
        take_profit={'limit_price': take_profit_price}
    )

    # Execute bracket order
    trading_client.submit_order(market_order_request)