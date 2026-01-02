# This file contains configuration settings for the project.
# API endpoints, parameters, and data paths.

# World Bank API base URL
WORLD_BANK_API_URL = "https://api.worldbank.org/v2"

# API Parameters
API_PARAMS = {
    "format": "json",
    "per_page": 100, # Number of records per page
    "date": "2000:2020" # Date range for data
}

# Data paths
data_paths = {
    "raw": "data/raw",
    "processed": "data/processed",
    "features": "data/features",
    "forecasts": "data/forecasts"
}

# Logging path
LOGGING_PATH = "logs/gderis.log"