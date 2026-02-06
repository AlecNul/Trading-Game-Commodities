import json
import yfinance as yf
import os

# Path handling
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_config_path = os.path.join(project_root, 'config', 'data_config.json')
data_dir = os.path.join(project_root, 'data')

# Ticker Configuration
with open(data_config_path, 'r') as f:
    config = json.load(f)

all_tickers = [config['futures']] + config['etfs'] + config['equities']
start_date = config['start_date']

# Data Downloading
print("Downloading...")
data = yf.download(all_tickers, start=start_date, interval="1d", auto_adjust=False) # We'll use 2 headers for the CSV

df_final = data.dropna()

# CSV Creation
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

output_path = os.path.join('data', 'dataset_G21.csv')
df_final.to_csv(output_path)

print(f"Dataset added in data")
print(f"Dataset size : {df_final.shape}")