
from fastapi import FastAPI
from models.user import User
# from dotenv import load_dotenv
from pymongo import MongoClient
import logging
import os

# load_dotenv()

# Connect to database when running the app
async def get_database():
    """Dependency function to access the database in routes."""
    # mongo_uri = os.getenv("MONGO_URI")
    mongo_uri = "mongodb+srv://testUser:testUser123@ticketgenerator.o9p58.mongodb.net/"
    client = MongoClient(mongo_uri)

    db = client.da_hack
    # print(db)
    return db
