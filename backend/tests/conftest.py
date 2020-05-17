# ----- Graphene Client example
# tests/conftest.py
import pytest
from graphene.test import Client

from app.main import schema


@pytest.fixture(scope="module")
def graphql_client():
    return Client(schema)


# # Starlette TestClient example
# import pytest
# from starlette.testclient import TestClient

# from app.main import app


# @pytest.fixture(scope="module")
# def test_app():
#     client = TestClient(app)
#     yield client  # testing happens here
