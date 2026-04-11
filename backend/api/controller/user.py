from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from firebase_admin import auth

from api.firebase import db
from api.permission import AdminPermissions

from api.controller.design.idfactory import IdFactory
from .design import check_command

# Api-Key ho4f2fm2.WYyNAfuaYikL9QvUycDIz41FD1G18zEc - Admin

@api_view(['POST'])
@permission_classes([AdminPermissions])
def create_user(request):
    factoryId = IdFactory(allow_letters=True, length=15)
    data = request.data

    if not data['email']:
        return Response({
            'success': False,
            'message': "require email field"
        }, status=status.HTTP_400_BAD_REQUEST)

    # check if email is valid 
    emailChecker = check_command.CheckEmailCommand(data["email"])
    invoker = check_command.Invoker()
    invoker.set_command(emailChecker)

    if not invoker.execute_command():
        return Response({
            'success': False,
            "message": "Not a valid email"
        }, status=status.HTTP_400_BAD_REQUEST)

    # --- for authentication database --- 



    doc_ref = db.collection('users').document()
    doc_ref.set({
        "username": data['username'],
        "cesPoints": data['cesPoints'],
        "id": factoryId.create_id(),
        'email': data["email"]
    })

    return Response({
        'success': True,
        'message': data
    }, status=status.HTTP_201_CREATED)
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status

# # 1. This is the missing line!

# from api.firebase import db
# from api.permission import AdminPermissions

# @api_view(['POST'])
# @permission_classes([AdminPermissions])

# def create_user(request):
#     """
#         creates a user from the firebase data
#         Args:
#             request (Request): The DRF request object containing user data in the body.
#         Permissions:
#             - Requires BasePermissions (Valid API Key).
#         Returns:
#             - Response: A Json Object containing UID of where data is located, and meessage     
#     """
#     data = request.data

#     if not data.get("email"):
#         return Response({
#             'success': False,
#             'message': "Email Field required"
#         }, status=status.HTTP_400_BAD_REQUEST)

#     doc_ref = db.collection('users').document()
#     doc_ref.set({
#         "name": data["name"],
#         "email": data["email"],
#     })

#     return Response({"id": doc_ref.id, "message": "User created"}, status=201)

