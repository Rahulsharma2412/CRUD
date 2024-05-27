import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]
myquery = {"address" : {"$gt" : "x"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)