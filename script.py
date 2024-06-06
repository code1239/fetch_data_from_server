import requests
import json
from datetime import datetime
from typing import List, Dict, Any
import schedule
import logging
import time
import configparser

# Load the configuration
config = configparser.ConfigParser()
config.read('config.ini')
SERVER_URL = config['commands']['SERVER_URL']



# Configure logging
logging.basicConfig(filename='log_file.log', level=logging.INFO, 
                    format='%(levelname)s - %(message)s')

def fetch_data_from_server(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_data(data):
    for record in data:
        record['timestamp'] = datetime.now().isoformat()
    return data

def save_data_to_json(data, filename: str):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logging.info(f"Data saved to {filename}")

def main():
    logging.info("Starting the automation script...")
    data = fetch_data_from_server(SERVER_URL)
    logging.info(f"Fetched {len(data)} records")
    processed_data = process_data(data)
    logging.info("Data processing complete.")
    save_data_to_json(processed_data, "processed_data.json")
    logging.info("Automation script completed successfully.")

if __name__ == "__main__":
    main() 
    schedule.every(1).minute.do(main)

    while True:
        time.sleep(1)
        schedule.run_pending()
