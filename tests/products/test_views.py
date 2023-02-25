import http
from unittest import mock

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
        self.monkeypatch.setattr(views, "products_collection", MongoDbCollectionMock([]))
        response = self.client.get("/products/")

        assert response.status_code == http.HTTPStatus.OK

    def test_view_returns_expected_output_without_objects(self):
        self.monkeypatch.setattr(views, "products_collection", MongoDbCollectionMock([]))
        response = self.client.get("/products/")

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

        response = self.client.get("/products/")

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
        response = self.client.get("/products/")

        assert response.json() == expected_output

    def test_view_returns_http_created_response_for_post_request_with_correct_body(self):
        body = {
            "name": "Product 1",
            "description": "Product 1 description",
            "price": 11.0,
            "quantity": 2,
        }
        self.monkeypatch.setattr(views, "products_collection", MongoDbCollectionMock())
        response = self.client.post("/products/", json=body)

        assert response.status_code == http.HTTPStatus.CREATED

    def test_view_returns_correct_message_for_post_request_with_correct_body(self):
        body = {
            "name": "Product 1",
            "description": "Product 1 description",
            "price": 11.0,
            "quantity": 2,
        }
        self.monkeypatch.setattr(views, "products_collection", MongoDbCollectionMock())
        response = self.client.post("/products/", json=body)

        assert response.json() == {"message": "Created", "body": body}

    @mock.patch("src.products.views.products_collection", new_callable=mock.AsyncMock)
    def test_view_calls_insert_one_with_correct_arguments(self, products_collection_mock):
        body = {
            "name": "Product 1",
            "description": "Product 1 description",
            "price": 11.0,
            "quantity": 2,
        }
        self.client.post("/products/", json=body)

        assert products_collection_mock.insert_one.call_args == ((body,),)

    def test_view_returns_http_bad_request_response_for_post_request_with_incorrect_body(self):
        body = {
            "name": "Product 1",
            "description": "Product 1 description",
            "price": 11.0,
        }
        self.monkeypatch.setattr(views, "products_collection", MongoDbCollectionMock())
        response = self.client.post("/products/", json=body)

        assert response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

    def test_view_returns_http_conflict_status_for_post_request_with_duplicate_name(self):
        body = {
            "name": "Product 1",
            "description": "Product 1 description",
            "price": 11.0,
            "quantity": 2,
        }
        self.monkeypatch.setattr(
            views,
            "products_collection",
            MongoDbCollectionMock(duplicate_key_error=True),
        )
        response = self.client.post("/products/", json=body)

        assert response.status_code == http.HTTPStatus.CONFLICT

    def test_view_returns_correct_message_for_post_request_with_duplicate_name(self):
        body = {
            "name": "Product 1",
            "description": "Product 1 description",
            "price": 11.0,
            "quantity": 2,
        }
        self.monkeypatch.setattr(
            views,
            "products_collection",
            MongoDbCollectionMock(duplicate_key_error=True),
        )
        response = self.client.post("/products/", json=body)

        assert response.json() == {
            "message": "Duplicated",
            "body": "product with name 'Product 1' already exists",
        }
