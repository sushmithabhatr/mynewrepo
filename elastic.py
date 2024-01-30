from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://...",  # Elasticsearch endpoint
    api_key=('api-key-id', 'api-key-secret'),  # API key ID and secret
)
