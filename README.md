# Automated Data Processing Script

This Python script automates the task of fetching data from a server, processing it, and saving it to a JSON file. The script runs continuously, fetching new data from a server endpoint defined in the `config.ini` file every minute.

## Usage

1. Install the necessary Python packages using `pip install -r requirements.txt`.
2. Customize the `config.ini` file to specify the server URL.
3. Run the script using `python automate_background_task.py`.
4. The script will start fetching data from the specified server URL, process it by adding timestamps, and save it to a JSON file named `processed_data.json`.

## Configuration

- The server URL is specified in the `config.ini` file.
- Logging is configured to write logs to `log_file.log`.
- Processed data is saved to `processed_data.json`.

## Dependencies

- requests
- schedule

