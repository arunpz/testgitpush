import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron2:admirer123@cluster0.bsvi5r3.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)



d={"name":"arun",
   "email":"arunpz@gmail.com",
   "surname":"pratap"
}

db1=client['mongotest']  #databse
coll = db1['test']
coll.insert_one(d)