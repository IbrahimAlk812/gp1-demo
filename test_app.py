from app import app

def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_bus_location():
    client = app.test_client()
    response = client.get("/bus/location")
    assert response.status_code == 200
    assert "location" in response.get_json()

def test_bus_capacity():
    client = app.test_client()
    response = client.get("/bus/capacity")
    assert response.status_code == 200
    assert "capacity" in response.get_json()
