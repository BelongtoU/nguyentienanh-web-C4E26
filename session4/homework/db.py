from pymongo import MongoClient

uri = "mongodb+srv://gate_1:tienanh@c4e-qeuwg.mongodb.net/test?retryWrites=true"

# connect
client = MongoClient(uri)

# get database
db = client.test # web default

# get collection
user_collection = db["user"]

 
# new_acc = {
#     "username": "PhongTienNguyen",
#     "passwords": "ourtownsobeautiful"
# }

# u_list = user_collection.find({})
# for i in range(3):
#     print(u_list[i]["username"])



#close connecction
def close():
    client.close()