import os
import requests
import time
import json
import logging
from dotenv import load_dotenv

# Get information for .env file
load_dotenv()

# LOKI Configurations
LOKI_URL = os.getenv("LOKI_URL")
USERNAME = os.getenv("USERNAME_LOKI")
API_KEY = os.getenv("API_KEY")

logging.basicConfig(level=logging.INFO)


def send_log_loki(message, level="info", job="python-rpa"):
    timestamp = str(int(time.time() * 1e9))  # nanoseconds
    payload = {
        "streams": [
            {
                "stream": {
                    "job": job,
                    "level": level
                },
                "values": [
                    [timestamp, message]
                ]
            }
        ]
    }

    response = requests.post(
        LOKI_URL,
        auth=(USERNAME, API_KEY),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    if response.status_code != 204:
        logging.error(f"Error sending log to Loki: {response.status_code} - {response.text}")
    else:
        logging.info(f"Log sent: {message}")


if __name__ == "__main__":
    send_log_loki("RPA starting...", "info")
    send_log_loki("RPA error...", "error")
    send_log_loki("RPA successfully completed", "info")
