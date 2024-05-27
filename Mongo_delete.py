import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]

myquery = { "address": "Highway 37" }

mycol.delete_one(myquery)