import firebase_admin
from firebase_admin import credentials, firestore

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

JSON_PATH = os.path.join(BASE_DIR, "private", "firebase_connect.json")

cred = credentials.Certificate(JSON_PATH)
firebase_admin.initialize_app(cred)
db = firestore.client()