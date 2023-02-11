import http

from fastapi.testclient import TestClient

from src.main import app


class TestProductsViews:
    @classmethod
    def setup_class(cls):
        cls.client = TestClient(app)

    def test_view_returns_https_ok_response(self):
        response = self.client.get("/products")

        assert response.status_code == http.HTTPStatus.OK

    def test_view_returns_expected_output_without_objects(self):
        response = self.client.get("/products")

        assert response.json() == []

    def test_view_returns_expected_output_for_single_object(self):
        response = self.client.get("/products")
        expected_output = [
            {
                "name": "Product 1",
                "price": 10,
            }
        ]

        assert response.json() == expected_output

    def test_view_returns_expected_output_for_multiple_object(self):
        response = self.client.get("/products")
        expected_output = [
            {
                "name": "Product 1",
                "price": 10,
            },
            {
                "name": "Product 2",
                "price": 20,
            },
            {
                "name": "Product 3",
                "price": 30,
            },
        ]

        assert response.json() == expected_output
