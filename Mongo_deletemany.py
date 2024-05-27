import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]

myquery = { "address": {"$regex": "^C"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")