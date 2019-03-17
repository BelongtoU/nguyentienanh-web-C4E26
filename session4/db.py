from pymongo import MongoClient

uri = "mongodb+srv://gate_1:tienanh@c4e-qeuwg.mongodb.net/test?retryWrites=true"

# connect
client = MongoClient(uri)

# get database
db = client.test # web default

# get collection
food_collection = db["food"]

# new_food = {
#     "name": "bun cha",
#     "price": 30000, 
# }
#  #insert new food
# food_collection.insert_one(new_food)


#close connecction
def close():
    client.close()