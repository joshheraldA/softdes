import os
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # points to backend/api/
    cred_path = os.path.join(BASE_DIR, "private", "joshdoctorplayhouse-firebase-adminsdk-fbsvc-c8835ec406.json")
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()