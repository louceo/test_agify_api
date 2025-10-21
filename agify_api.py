import requests

def test_agify_api():
    response = requests.get("https://api.agify.io?name=Dave")
    assert response.status_code == 200
    data = response.json()
    assert "age" in data 
    assert isinstance(data["age"], int)
    