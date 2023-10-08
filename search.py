import pymongo

# https://www.w3schools.com/python/python_mongodb_find.asp
myclient = pymongo.MongoClient("mongodb+srv://lkara4:oaj2612ceW85TxlR@cluster1.ctkteaw.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["clueExport"]
mycol = mydb["questions"]

x = mycol.find_one()

print(x)

