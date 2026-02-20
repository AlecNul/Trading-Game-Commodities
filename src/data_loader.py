import json
import yfinance as yf
import os

def load_csv(start_date="2020-01-01", end_date="2025-12-31", write=False):
    # Path handling
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_config_path = os.path.join(project_root, 'config', 'data_config.json')
    data_dir = os.path.join(project_root, 'data')

    # Ticker Configuration
    with open(data_config_path, 'r') as f:
        config = json.load(f)

    all_tickers = config['futures'] + config['etfs'] + config['equities'] + config['forex'] + config['softs']

    # Data Downloading
    # print("Downloading data...")
    data = yf.download(all_tickers, start=start_date, end=end_date, interval="1d", auto_adjust=False) # We'll use 2 headers for the CSV

    if write:
        # CSV Creation
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        output_path = os.path.join(data_dir, 'dataset_G21.csv')
        data.to_csv(output_path)

    # print(f"Done.")
    # print(f"Dataset size : {df_final.shape}")
    return data