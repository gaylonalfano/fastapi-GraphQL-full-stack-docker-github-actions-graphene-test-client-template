import graphene
from graphql.execution.executors.asyncio import AsyncioExecutor
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from fastapi.routing import APIRoute


class Query(graphene.ObjectType):
    # Define a Field 'hello' in our Schema with a single Argument 'name'
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    # Resolver method takes GraphQL context (root/self/parent, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    # Type hints: For instance methods, omit type for "self"
    # JS/Prisma equivalent: (obj/parent, args, context, info)
    async def resolve_hello(self, info, name):
        # We can make asynchronous network calls here
        return f"Hello {name}"


# Explicity define schema so can use in conftest.py. There may be a better way.
schema = graphene.Schema(query=Query)

# Define our routes following Starlette's example
routes = [
    # We're using 'executor_class=AsyncioExecutor' here.
    # Route("/", GraphQLApp(schema=schema, executor_class=AsyncioExecutor))
    APIRoute("/", GraphQLApp(schema=schema, executor_class=AsyncioExecutor))
]

app = FastAPI(routes=routes)
# app.add_route("/", GraphQLApp(schema=schema))
# app.add_route(
#     "/", GraphQLApp(schema=schema, executor_class=AsyncioExecutor),
# )

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


# @app.get("/ping")
# async def pong():
#     # some async operation could happen here
#     # example: `notes = await get_all_notes()`
#     return {"ping": "pong!"}


# # Here's a super long comment that will eventually trigger an issue with flake8.
