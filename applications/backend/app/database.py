from azure.cosmos import CosmosClient
import os

COSMOS_ENDPOINT = os.getenv("https://cloudmart-db-1893556.documents.azure.com:443/")
COSMOS_KEY = os.getenv("IE2Fj336sI1SAyptJQUyMqwWQtae4FqX7pmeg5DngstNVeKSZQK7EokfRUPxVwUc8GApkvInS6XwACDbsFQCrA==")
DATABASE_NAME = "cloudmart"

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.create_database_if_not_exists(id=DATABASE_NAME)

products_container = database.create_container_if_not_exists(
    id="products",
    partition_key="/category",
    offer_throughput=400
)
cart_container = database.create_container_if_not_exists(
    id="cart",
    partition_key="/user_id",
    offer_throughput=400
)
orders_container = database.create_container_if_not_exists(
    id="orders",
    partition_key="/user_id",
    offer_throughput=400
)
