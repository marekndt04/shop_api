import http

import pytest
from fastapi.testclient import TestClient

import src.products.views as views
from src.main import app
from tests.db_mock_interface import MongoDbCollectionMock


class TestProductsViews:
    @classmethod
    @pytest.fixture(autouse=True)
    def setup_class(cls, monkeypatch):
        cls.client = TestClient(app)
        cls.monkeypatch = monkeypatch

    def test_view_returns_https_ok_response(self):
        response = self.client.get("/products")

        assert response.status_code == http.HTTPStatus.OK

    def test_view_returns_expected_output_without_objects(self):
        self.monkeypatch.setattr(views, "products_collection", MongoDbCollectionMock([]))
        response = self.client.get("/products")

        assert response.json() == []

    def test_view_returns_expected_output_for_single_object(self):
        expected_output = [
            {
                "name": "Product 1",
                "description": "Product 1 description",
                "price": 10.0,
                "quantity": 1,
            }
        ]
        self.monkeypatch.setattr(
            views, "products_collection", MongoDbCollectionMock(expected_output)
        )

        response = self.client.get("/products")

        assert response.json() == expected_output

    def test_view_returns_expected_output_for_multiple_object(self):
        expected_output = [
            {
                "name": "Product 1",
                "description": "Product 1 description",
                "price": 11.0,
                "quantity": 2,
            },
            {
                "name": "Product 2",
                "description": "Product 2 description",
                "price": 13.0,
                "quantity": 3,
            },
            {
                "name": "Product 3",
                "description": "Product 3 description",
                "price": 14.0,
                "quantity": 4,
            },
        ]
        self.monkeypatch.setattr(
            views, "products_collection", MongoDbCollectionMock(expected_output)
        )
        response = self.client.get("/products")

        assert response.json() == expected_output
