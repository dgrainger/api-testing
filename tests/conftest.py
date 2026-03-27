from collections.abc import Iterator
import os
import pytest
import httpx
from tests.settings import BASE_URL, join_url

@pytest.fixture(scope="session")
def api_root() -> str:
    protocol = os.getenv("API_PROTOCOL", "http")
    host = os.getenv("API_HOST", "localhost")
    port = os.getenv("API_PORT", "8080")
    return f"{protocol}://{host}:{port}{BASE_URL}"

@pytest.fixture(scope="session")
def client() -> Iterator[httpx.Client]:
    timeout = httpx.Timeout(60.0)
    with httpx.Client(timeout=timeout) as c:
        yield c

@pytest.fixture(scope="session")
def url(api_root: str):
    def build_url(path: str) -> str:
        return join_url(api_root, path)
    return build_url
