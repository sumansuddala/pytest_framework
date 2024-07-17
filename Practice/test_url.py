import requests
import pytest
import json

def test_request():
    url = "https://cat-fact.herokuapp.com/facts/"
    response = requests.request("GET", url)
    assert response.status_code == 200
