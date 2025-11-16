import requests
import urllib3

def fetch_status(url: str) -> int:
    r = requests.get(url, timeout=5)
    return r.status_code