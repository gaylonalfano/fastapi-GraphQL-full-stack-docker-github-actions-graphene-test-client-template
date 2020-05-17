# tests/test_main.my
from graphql.execution.executors.asyncio import AsyncioExecutor

# Don't think I have to import graphql_client since it's a fixture
# May not even need to import Client from graphene.test either!
# To test async:https://gitter.im/tiangolo/fastapi?at=5d19c94d490abf627a5428c6
# def test_hey(event_loop):
#     client = Client(my_schema)
#     executed = client.execute("""{ hey }""", executor=AsyncioExecutor())
#     import pdb

#     pdb.set_trace()
#     assert executed == {"data": {"hey": "hello!"}}


# def test_main_graphql(graphql_client):
#     executed = graphql_client.execute("""{ hello }""")
#     assert executed == {"data": {"hello": "Hello stranger"}}


# def test_main_graphql(graphql_client):
#     executed = graphql_client.execute("""{ hello(name: "Archie") }""")
#     assert executed == {"data": {"hello": "Hello Archie"}}


# Using snapshottest PLUS AsyncioExecutor
def test_main_graphql(snapshot, graphql_client):
    """
    This will create a snapshot dir and a snapshot file
    the first time the test is executed, with the response
    of the execution.
    """
    executed = graphql_client.execute(
        """{ hello(name: "Archie") }""", executor=AsyncioExecutor()
    )
    snapshot.assert_match(executed)


# # Using snapshottest
# def test_main_graphql(snapshot, graphql_client):
#     """
#     This will create a snapshot dir and a snapshot file
#     the first time the test is executed, with the response
#     of the execution.
#     """
#     executed = graphql_client.execute("""{ hello(name: "Archie") }""")
#     snapshot.assert_match(executed)
#     # assert executed == {"data": {"hello": "Hello Archie"}}


# from starlette.testclient import TestClient

# from app.main import app

# client = TestClient(app)
# # client = Client(app)


# def test_main_graphql_get(test_app):
#     """Using Starlette Test Client"""
#     response = test_app.get(url="/?query={ hello }")
#     assert response.status_code == 200
#     assert response.json() == {"data": {"hello": "Hello stranger"}}


# def test_ping(test_app):
#     response = test_app.get("/ping")
#     assert response.status_code == 200
#     assert response.json() == {"ping": "pong!"}
