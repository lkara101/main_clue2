from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://lkara4:oaj2612ceW85TxlR@cluster1.ctkteaw.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.gettingStarted
people = db.people

import datetime
personDocument = {
  "name": { "first": "Alan", "last": "Turing" },
  "birth": datetime.datetime(1912, 6, 23),
  "death": datetime.datetime(1954, 6, 7),
  "contribs": [ "Turing machine", "Turing test", "Turingery" ],
  "views": 1250000
}

people.insert_one(personDocument)
people.find_one({ "name.last": "Turing" })


