from flask import request, Blueprint
from flask_cors import cross_origin

from service import stock_trading_service
import json

stock_trading_controller_blueprint = Blueprint('stock_trading_controller_blueprint', __name__)


@stock_trading_controller_blueprint.route('/api/fetch-stock-list')
@cross_origin()
def fetch_stock_list():
    return stock_trading_service.fetch_stock_list()


@stock_trading_controller_blueprint.route('/api/update-stock-list', methods=['PUT'])
@cross_origin()
def update_stock_list():
    return stock_trading_service.update_stock_list(json.loads(request.data))


@stock_trading_controller_blueprint.route('/api/fetch-traded-stock-info-list')
@cross_origin()
def fetch_traded_stock_info_list():
    return stock_trading_service.fetch_traded_stock_info_list()


@stock_trading_controller_blueprint.route('/api/run-ml-model', methods=['POST'])
@cross_origin()
def run_ml_model():
    return stock_trading_service.run_ml_model()


@stock_trading_controller_blueprint.route('/api/run-trading-system', methods=['POST'])
@cross_origin()
def run_trading_system():
    return stock_trading_service.run_trading_system()


