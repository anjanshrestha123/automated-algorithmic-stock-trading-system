import pickle
from config import config
import numpy as np


def read_model_output(stock_ticker):
    with open(config.get_model_output_path(stock_ticker), 'rb') as f:
        model_output = pickle.load(f)
    return model_output


def predict_stock_price(stock_ticker, no_of_predictions):
    print('Predicting stock prices for [{}] for next [{}] intervals'.format(stock_ticker, no_of_predictions))

    # Read model output
    model_output = read_model_output(stock_ticker)

    # Store the values into different variables
    model = model_output['trained_model']
    rmse = model_output['rmse']
    latest_interval_data = model_output['latest_interval_data']
    scaler = model_output['scaler']

    predicted_prices = []

    for i in range(no_of_predictions):
        # Make prediction for next interval
        last_n_days_data = latest_interval_data.reshape(latest_interval_data.shape[1], latest_interval_data.shape[0], 1)
        prediction = model.predict(last_n_days_data)
        transformed_prediction = scaler.inverse_transform(prediction)

        # Prepare data for next prediction
        latest_interval_data = np.delete(latest_interval_data, 0, 0)
        latest_interval_data = np.append(latest_interval_data, prediction, axis=0)

        # Store prediction values
        predicted_prices.append(transformed_prediction[0][0])

    print('Predicted stock prices for [{}] are {}'.format(stock_ticker, predicted_prices))
    return predicted_prices


