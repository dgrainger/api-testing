import os

BASE_URL = os.getenv("API_CONTEXT_ROOT", "")

def join_url(root: str, path: str) -> str:
    return root.rstrip("/") + "/" + path.lstrip("/")
