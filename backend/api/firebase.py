from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import firebase_admin
from firebase_admin import credentials, firestore
import os 


cred = credentials.Certificate("/Users/twsty/Documents/jfet joshs field effect transistor/softdes/backend/api/private/joshywoshy.json")
firebase_admin.initialize_app(cred)
db = firestore.client()