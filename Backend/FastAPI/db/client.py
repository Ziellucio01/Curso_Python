from pymongo import MongoClient

# db_client = MongoClient().local # Base de datos local


#  Base de datos remota

db_client = MongoClient(
    "mongodb+srv://test:test@cluster0.hfm52kp.mongodb.net/?retryWrites=true&w=majority").test
