import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myfirst = myclient["Rahul"]
mycol = myfirst["Sharma"]

myresult = mycol.find().limit(5)

#print the result:
for x in myresult:
  print(x)