from app import app


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    if response.status_code != 200:
        raise AssertionError(f"Expected 200 but got {response.status_code}")


def test_bus_location():
    client = app.test_client()
    response = client.get("/bus/location")

    if response.status_code != 200:
        raise AssertionError(f"Expected 200 but got {response.status_code}")

    data = response.get_json()
    if "location" not in data:
        raise AssertionError("Response JSON missing 'location' key")


def test_bus_capacity():
    client = app.test_client()
    response = client.get("/bus/capacity")

    if response.status_code != 200:
        raise AssertionError(f"Expected 200 but got {response.status_code}")

    data = response.get_json()
    if "capacity" not in data:
        raise AssertionError("Response JSON missing 'capacity' key")
