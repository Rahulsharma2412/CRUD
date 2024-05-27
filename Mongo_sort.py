import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)