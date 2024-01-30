from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://...",  # Elasticsearch endpoint
    api_key=('api-key-id', 'api-key-secret'),  # API key ID and secret
)

###python elastic extender###

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

doc = {
    "author": "kimchy",
    "text": "Elasticsearch: cool. bonsai cool.",
    "timestamp": datetime.now(),
}
resp = es.index(index="test-index", id=1, document=doc)
print(resp["result"])

resp = es.get(index="test-index", id=1)
print(resp["_source"])

es.indices.refresh(index="test-index")

resp = es.search(index="test-index", query={"match_all": {}})
print("Got {} hits:".format(resp["hits"]["total"]["value"]))
for hit in resp["hits"]["hits"]:
    print("{timestamp} {author} {text}".format(**hit["_source"]))
