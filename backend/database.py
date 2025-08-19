from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["video_scraper"]   # database
videos_collection = db["videos"]   # collection
