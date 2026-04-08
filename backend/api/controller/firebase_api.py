# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.firebase import db

@api_view(['POST'])
def create_user(request):
    data = request.data  # { "name": "Sam", "email": "sam@email.com" }

    # validate here
    if not data.get("email"):
        return Response({"error": "email required"}, status=400)

    # write to Firestore
    doc_ref = db.collection("users").document()
    doc_ref.set({
        "name": data["name"],
        "email": data["email"],
    })

    return Response({"id": doc_ref.id, "message": "User created"}, status=201)