# create documents
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient(
    'mongodb+srv://VOliinyk:XtgdQ9Eg5wrg0RF7@cluster0.z6ynvxw.mongodb.net/?retryWrites=true&w=majority'
)

db = client.MyDB

# result_one = db.employees.insert_one(
#     {
#         "name": "Vasyl Reminski",
#         "age": 33,
#         "building": 2
#     }
# )

# print(result_one.inserted_id)

# result_many = db.employees.insert_many(
# [
#     {
#         "name": "Timur Mutsuraev",
#     "age" : 52,
#     "building": 1
#     },
#     {
#     "name": "Slawoi Jejek",
#     "age": 55,
#     "role": "writer",
#     "building": 1
#     }

# ]

# )

# Get documents

# result = db.employees.find_one({"name": 'Slawoi Jejek'})
# print(result)
    
# # Get many documents

# result = db.employees.find({})
# for el in result:
#     print(el)

# # Update documents
# #update_one

# db.employees.update_one({"name": "Slawoi Jejek"},{"$set": {"age": 43}})
# result = db.employees.find_one({"name": "Slawoi Jejek"})
# print(result)

# # Delete documents

# db.employees.delete_one({"name": "Igor Jons"})
# result = db.employees.find_one({"name": "Igor Jons"})
# print(result)
