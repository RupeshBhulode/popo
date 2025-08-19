from firebase_admin import credentials, firestore
import firebase_admin
import os
import json

# Load Firebase credentials from environment variable
firebase_key_json = os.environ.get("FIREBASE_KEY")
if not firebase_key_json:
    raise ValueError("FIREBASE_KEY environment variable not set")

cred = credentials.Certificate(json.loads(firebase_key_json))
firebase_admin.initialize_app(cred)

db = firestore.client()
videos_collection = db.collection("videos")
