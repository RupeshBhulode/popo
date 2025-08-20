from firebase_admin import credentials, firestore
import firebase_admin
import os
import json

# Load Firebase credentials from environment variable
firebase_key_json = os.environ.get("FIREBASE_KEY")
if not firebase_key_json:
    raise ValueError("FIREBASE_KEY environment variable not set")

# Parse JSON and fix the private_key formatting
firebase_key_dict = json.loads(firebase_key_json)
firebase_key_dict['private_key'] = firebase_key_dict['private_key'].replace('\\n', '\n')

# Initialize Firebase app
cred = credentials.Certificate(firebase_key_dict)
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()
videos_collection = db.collection("videos")

