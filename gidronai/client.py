import httpx
from typing import Optional

class GidronClient:
    BASE_URL = "https://api.gidronai.me/v1"

    def __init__(self, api_key: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url or self.BASE_URL
        self._http = httpx.Client(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
        self.scenes = SceneManager(self._http)
        self.datasets = DatasetManager(self._http)

    def close(self):
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

class SceneManager:
    def __init__(self, http):
        self._http = http

    def create(self, environment: str, **kwargs):
        from .scene import Scene
        resp = self._http.post("/scenes", json={"environment": environment, **kwargs})
        resp.raise_for_status()
        return Scene(self._http, resp.json())

    def list(self, limit: int = 50):
        resp = self._http.get("/scenes", params={"limit": limit})
        resp.raise_for_status()
        return resp.json()["scenes"]

class DatasetManager:
    def __init__(self, http):
        self._http = http

    def list(self, limit: int = 50):
        resp = self._http.get("/datasets", params={"limit": limit})
        resp.raise_for_status()
        return resp.json()["datasets"]
