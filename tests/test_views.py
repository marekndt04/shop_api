from fastapi.testclient import TestClient

from src.main import app


class TestHealtCheckView:
    def setup_method(self):
        self.client = TestClient(app)

    def test_view_returns_http_ok_response(self):
        response = self.client.get("/healthcheck")
        assert response.status_code == 200
        assert response.json() == {}
