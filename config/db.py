from pymongo import MongoClient

MONGO_URI = "mongodb+srv://armeennadeem9:yourpassword@cluster0.te5qatu.mongodb.net/library?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["library"]
books_collection = db["books"]
