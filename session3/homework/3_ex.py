from pymongo import MongoClient
from matplotlib import pyplot as p



uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

all_clt = MongoClient(uri).c4e

customers_clt = all_clt["customers"]

def count (key, value):
    customers_l = customers_clt.find(
        {
            key: value,
        }
    )
    return customers_l.count()

ads_c = count("ref", "ads")
wom_c = count("ref", "wom")
events_c = count("ref", "events")

#count the number of customers group by 'ref'
print("The number of customers group by 'ads' is:", ads_c)
print("The number of customers group by 'wom' is:", wom_c)
print("The number of customers group by 'events' is:", events_c)

#draw pie chart (let comment previous action to check the script below :)))
data = [ads_c, wom_c, events_c]
labels = ["Advertisements", "Words of mouth", "Events"]
colors = ["red", "blue", "yellow"]


p.pie(data, explode= None, labels= labels, colors= colors, autopct= '%1.1f%%', shadow= True,)
p.axis("equal")
p.show()