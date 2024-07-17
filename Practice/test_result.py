import requests


def test_request1():
    url = "https://cat-fact.herokuapp.com/facts/"
    response = requests.request("GET", url)
    resp = response.json()
    print('Response: ', response)
    print('Resp: ', resp)
    assert response.status_code == 200

def test_request2():
    url = "https://api.restful-api.dev/objects"
    response = requests.request("GET", url)
    resp = response.json()
    print('Response: ', response)
    print('Resp: ', resp)
    assert response.status_code == 200
