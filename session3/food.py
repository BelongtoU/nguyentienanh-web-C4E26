from db import food_collection, close

def add_food (name, price):
        new_food = {
            "name": name,
            "price": price
        }
        food_collection.insert_one(new_food)


def get():
    food_list = food_collection.find()
    return food_list

if __name__ == "__main__":
    # while True:
    #     n = input("Name: ")
    #     p = int(input("Price: "))
    #     add_food(n, p)
    # close()
    food_list = food_collection.find(
        {
            "price": {"$gt": 25000}
        }
    )          # lazy loading
    
    
    for food in food_list:
        print(food["name"])
        print(food["price"])
