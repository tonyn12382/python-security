import pytest
from src.app import fetch_status

def test_fetch_status_ok():
    # httpbin.org provides predictable responses for testing
    assert fetch_status("https://httpbin.org/status/200") == 200

def test_fetch_status_not_found():
    assert fetch_status("https://httpbin.org/status/404") == 404
