from db import food_collection
from bson import ObjectId

def add_food (name, price):
        new_food = {
            "name": name,
            "price": price
        }
        food_collection.insert_one(new_food)


def get (query):
    food_list = food_collection.find(query)
    return food_list

def get_by_id(id):
    f = food_collection.find_one({ "_id": ObjectId(id) })
    return f 

def delete_by_id(id):
    food_collection.delete_one({ "_id": ObjectId(id) })

def update_by_id (id, name = 0, price = 0):
    if price != 0:
        food_collection.find_one_and_update({ "_id": ObjectId(id)}, { "$set": { "price": price } })
    if name != 0:
        food_collection.find_one_and_update({ "_id": ObjectId(id)}, { "$set": { "name": name } })




if __name__ == "__main__":
    # while True:
    #     n = input("Name: ")
    #     p = int(input("Price: "))
    #     add_food(n, p)
    # close()
    # food_list = food_collection.find(
    #     {
    #         "price": {"$gt": 25000}
    #     }
    # )          # lazy loading
    #add_food("bun cha", 30000)

    # if f != None:
    #     print(f["name"])
    # else:
    #     print("Not Found !!!")
    
    # updater: $inc, $dec, $set, $unset
    food_collection.find_one_and_update({ "_id": ObjectId("5c812908f346793bf4f455ea")}, { "$set": { "price": 10000 } } )
    print(*get({}), sep= "\n")