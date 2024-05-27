import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]

myquery = { "address": "Canyon 123" }
newvalues = { "$set": { "address": "Valley 345" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)
