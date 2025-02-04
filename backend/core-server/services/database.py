from pymongo import MongoClient

MONGO_URI = "<MONGO DB CONNECTION STRING>"

client = MongoClient(MONGO_URI)
db = client.da_hack
