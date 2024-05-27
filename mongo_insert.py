import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]


print(myclient.list_database_names())

mydict = { "name": "Rahul", "address": "Delhi" }

x = mycol.insert_one(mydict)

# for i in x:

for i in mycol.find({},{'_id':0}):
    print(i)