from pymongo import MongoClient
from matplotlib import pyplot as p



uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri).c4e

customers = client["customers"]

def count (key, value):
    customer_l = customers.find(
        {
            key: value,
        }
    )
    return customer_l.count()

ads_c = count("ref", "ads")
wom_c = count("ref", "wom")
events_c = count("ref", "events")

#draw pie chart
data = [ads_c, wom_c, events_c]
labels = ["Advertisements", "Words of mouth", "Events"]
colors = ["red", "blue", "yellow"]


p.pie(data, explode= None, labels= labels, colors= colors, autopct= '%1.1f%%',)
p.axis("equal")
p.show()