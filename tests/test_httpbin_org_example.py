import pytest

@pytest.mark.httpbin
def test_delete(client, url):
    my_url = url("/delete")
    response = client.delete(my_url)
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/delete"
    assert data["headers"]["Host"] == "httpbin.org"

@pytest.mark.httpbin
def test_get(client, url):
    my_url = url("/get")
    response = client.get(my_url)
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/get"
    assert data["headers"]["Host"] == "httpbin.org"

@pytest.mark.httpbin
def test_post(client, url):
    my_url = url("/post")
    response = client.post(my_url)
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/post"
    assert data["headers"]["Host"] == "httpbin.org"

@pytest.mark.httpbin
def test_patch(client, url):
    my_url = url("/patch")
    response = client.patch(my_url)
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert data["url"] == "https://httpbin.org/patch"
    assert data["headers"]["Host"] == "httpbin.org"
