import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:admirer123@cluster0.txdcmqk.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "arun",
    "email": "arun@gmail.com",
    "surname" : "pratap"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)