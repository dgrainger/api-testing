import pytest

@pytest.mark.httpbin
def test_delete(client, url):
    response = client.delete(url("/delete"))
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/delete"
    assert data["headers"]["Host"] == "httpbin.org"

@pytest.mark.httpbin
def test_get(client, url):
    response = client.get(url("/get"))
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/get"
    assert data["headers"]["Host"] == "httpbin.org"

@pytest.mark.httpbin
def test_post(client, url):
    response = client.post(url("/post"))
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/post"
    assert data["headers"]["Host"] == "httpbin.org"

@pytest.mark.httpbin
def test_patch(client, url):
    response = client.patch(url("/patch"))
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/patch"
    assert data["headers"]["Host"] == "httpbin.org"

@pytest.mark.httpbin
def test_basic_auth(client, url):
    username = "user"
    password = "password"
    response = client.get(url(f"/basic-auth/{username}/{password}"), auth=(username, password))
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["user"] == username
    assert data["authenticated"]
