# ex_4
from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

all_clt = MongoClient(uri).c4e
rivers_clt = all_clt["river"]

# ex_5
rivers_in_Africa = rivers_clt.find(
    {
        "continent": "Africa",
    }
)

# ex_6
rivers_in_S_America = rivers_clt.find(
    {
        "continent": "S. America",
        "length": {"$lt": 1000},
    }
)

