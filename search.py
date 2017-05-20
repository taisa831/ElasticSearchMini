import certifi
from elasticsearch.client import Elasticsearch

es = Elasticsearch(
        ["https://cb35af4e37890e33bd330e954f130550.ap-northeast-1.aws.found.io"],
        port=9243,
        http_auth="taisa831:mondorol6697",
        use_ssl=True,
        verify_certs=True,
        ca_certs=certifi.where()
    )

res = es.get(index="elasticmini", doc_type="users", id="1")['_source']
print(res)

#res = es.search(body="q=2017-05-20")
#print(res)