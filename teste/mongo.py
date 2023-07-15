import pymongo
from collections.abc import MutableMapping


client = MongoClient("mongodb+srv://<admin>:<admin>@cluster0.fuset1t.mongodb.net/?retryWrites=true&w=majority")

db = client['ufsm_grade']

collection = db["grade"]

documentos = collection.find()

for documento in documentos:
    print(documento)