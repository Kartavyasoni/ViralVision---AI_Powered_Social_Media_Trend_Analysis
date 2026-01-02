# Validation for API Responses

def validate_api_response(response):
    """Validate the API response structure."""
    if not response or 'data' not in response:
        raise ValueError("Invalid API response structure.")