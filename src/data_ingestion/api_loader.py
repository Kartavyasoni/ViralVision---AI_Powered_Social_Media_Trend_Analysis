# API Loader for World Bank Data.
# Uses requests to fetch data from the World Bank API.

import requests
from config import WORLD_BANK_API_URL
from validation import validate_api_response

def fetch_world_bank_data(indicator, params):
    """Fetch data from the World Bank API for a given indicator."""
    url = f"{WORLD_BANK_API_URL}/country/all/indicator/{indicator}"
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    
    data = response.json()
    validate_api_response(data)
    
    return data

def fetch_multiple_indicators(indicators, params):
    """Fetch data for multiple indicators."""
    all_data = {}
    for indicator in indicators:
        all_data[indicator] = fetch_world_bank_data(indicator, params)
    return all_data

if __name__ == "__main__":
    # Example usage
    indicators = ["SP.POP.TOTL", "NY.GDP.MKTP.CD"]
    params = {
        "format": "json",
        "per_page": 100,
        "date": "2000:2020"
    }
    
    data = fetch_multiple_indicators(indicators, params)
    print(data)