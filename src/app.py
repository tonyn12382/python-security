import requests

def fetch_status(url: str) -> int:
    """
    Fetch the HTTP status code for a given URL.
    Uses requests with a timeout to avoid hanging.
    """
    response = requests.get(url, timeout=5)
    return response.status_code
