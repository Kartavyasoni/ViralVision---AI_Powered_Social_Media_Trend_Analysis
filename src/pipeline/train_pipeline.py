# Training Pipeline
from src.data_ingestion.api_loader import fetch_data_from_api
from src.data_preprocessing.cleaning import handle_missing_values
from src.feature_engineering.development_features import calculate_growth_rate

def run_training_pipeline():
    """Run the end-to-end training pipeline."""
    # Example steps
    raw_data = fetch_data_from_api("https://api.worldbank.org/v2", params={})
    cleaned_data = handle_missing_values(raw_data)
    features = calculate_growth_rate(cleaned_data, "gdp")
    return features
