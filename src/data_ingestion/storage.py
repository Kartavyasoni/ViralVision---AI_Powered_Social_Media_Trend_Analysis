# Storage Utilities for Raw Data
import os
import json

def save_raw_data(data, filepath):
    """Save raw data to a JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)