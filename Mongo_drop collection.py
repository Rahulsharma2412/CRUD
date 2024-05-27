import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]

mycol.drop()