import pytest

@pytest.mark.petstore
def test_create_user(client, url):
    username = "darrell"
    password = "Password01!"
    payload = {
        "id": 0,
        "username": username,
        "firstName": "Darrell",
        "lastName": "Grainger",
        "email": "dgrainge@thoughtworks.com",
        "password": password,
        "phone": "416-555-1212",
        "userStatus": 0
    }
    response = client.get(url(f"/user/{username}"))
    if (response.status_code == 404):
        response = client.post(url("/user/createWithList"), json=[payload], headers={"Content-Type": "application/json"})
        assert response.status_code == 200
        data = response.json()
        assert data is not None
        assert data["code"] == 200
    
    response = client.get(url("/user/login"), params={"username": username, "password": password})
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    session = int(data["message"].split(":")[1])
    assert session > 0

    response = client.post(url("/user"), json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data is not None