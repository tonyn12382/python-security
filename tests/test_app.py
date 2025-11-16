from app import fetch_status

def test_fetch_status_ok():
    # A simple 200 source; swap if your environment blocks it
    assert fetch_status("https://httpbin.org/status/200") == 200