# python\_grafana\_loki
Send logs directly from Python to Grafana Loki via HTTP, without relying on Promtail or external agents.

## Overview
This project demonstrates how to push structured logs from a Python script to Grafana Loki using its HTTP API. It's useful for logging from Python-based automation (e.g., RPA, ETL, data pipelines) into your Grafana Cloud dashboards.

## Requirements

### Python Requirements
* Python 3.7 or higher
* `requests` package (install via `pip`)

### Grafana Cloud Requirements
* A **Grafana Cloud account**
* A **Grafana Cloud Loki stack** (free or paid tier)
* A **Loki API Key** with **Logs\:Push** permission
* Your **Loki instance ID** and **Loki endpoint URL**

## Grafana Configuration
1. **Create a Grafana Cloud account** (if you don’t already have one):
   [https://grafana.com/signup](https://grafana.com/signup)

2. **Set up a Loki stack** (one is included in the free plan):
   Navigate to **Cloud > Connections > Loki**

   * Copy the **Loki HTTP endpoint** (e.g. `https://logs-prod-000.grafana.net/loki/api/v1/push`)
   * Note your **Instance ID** (used as the username for authentication)

3. **Create an API key**:

   * Go to **Cloud > API Keys**
   * Click **New API Key**
   * Set the role to `Logs:Push`
   * Copy and save the key (you will use it as the password for authentication)


## Installation
1. **Clone the repository:**
git clone https://github.com/tonpizzi/python_grafana_loki.git
cd python_grafana_loki

2. **(Optional) Create and activate a virtual environment:**
# Create venv
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Or on Unix/Mac:
source venv/bin/activate

3. **Install dependencies:**
pip install -r requirements.txt

## Configuration
In the file `main.py`, configure the following constants:

LOKI_URL = "https://logs-prod-000.grafana.net/loki/api/v1/push"  # Replace with your actual URL
USERNAME = "123456"  # Your Loki instance ID
API_KEY = "your-api-key-here"  # API key with Logs:Push permission

## Usage
Run the script to send a test log:
python main.py

You should see a `204 No Content` response if the log was accepted.

## Viewing Logs in Grafana
1. Log into your Grafana Cloud dashboard
2. Go to **Explore**
3. Select your **Loki** data source
4. Use a query like:

{job="python-rpa"}

To filter the logs sent from this script.

## Project Structure
python_grafana_loki/
├── main.py             # Main script to send logs
├── requirements.txt    # Python dependencies
└── README.md           # This file

## License
This project is licensed under the [MIT License](LICENSE).

