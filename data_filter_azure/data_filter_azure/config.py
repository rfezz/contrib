import os

STORAGE_CONNECTION_STRING = os.environ.get("AZURE_STORAGE_CONNECTION_STRING", None)
TABLE_NAME = os.environ.get("TABLE_NAME", None)
COSMOSDB_ENDPOINT = os.environ.get("COSMOSDB_ENDPOINT", None)
COSMOSDB_PRIMARYKEY = os.environ.get("COSMOSDB_PRIMARYKEY", None)
COSMOSDB_DATABASE = 'opa'
IS_EMULATED = False