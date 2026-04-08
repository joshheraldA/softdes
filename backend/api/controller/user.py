from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from api.serializer import BaseUserSerializer
from api.model.user.baseuser import BaseUser
from api.model.user.adminuser import AdminUser
from api.model.leveledapikey import LeveledApiKey

from api.permission import BasePermissions, AdminPermissions

from .design.idfactory import Factory

# ADMIN - ho4f2fm2.WYyNAfuaYikL9QvUycDIz41FD1G18zEc
# USER - 9Q2O03bB.EXJDhwHn7zHbWsiVeLBE9ZnAJVQUJAjG

@api_view(['GET'])
@permission_classes([BasePermissions])
def get_user(request):
    """
        Retrive the data of all base users
        Args:
            request (Request): The DRF request object containing user data in the body.
        Permissions:
            - Requires BasePermissions (Valid API Key).
        Returns:
            - Response: A JSON object containing a list of all users and a success message.              
    """
    BaseUsers = BaseUser.objects.all()
    data = BaseUserSerializer(BaseUsers, many=True).data
    return Response({
        'success': True,
        'message': "Gucci ra",
        'data': data
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AdminPermissions])

def post_user(request):
    """
    Create a new BaseUser and generate a unique API Key.

    This function utilizes a Factory to generate a unique ID and automatically
    provisions a 'USER' level API key for the newly created account.

    Args:
        request (Request): The DRF request object containing user data in the body.

    Permissions:
        - Requires AdminPermissions (Admin-level API Key).

    Returns:
        Response: Created user data and the plain-text API key (shown only once).
    """
    serializer = BaseUserSerializer(data=request.data)

    factory = Factory(allow_letters=True)
    idnumber = factory.create_id()

    if serializer.is_valid():
        user = serializer.save(idNum=idnumber)
    
    api_key_name = f"Api-Key for ${user.username}"
    api_key_instance, key_token = LeveledApiKey.objects.create_key(
        name=api_key_name,
        user=user,
        level='USER'
    )

    return Response({
        'success': True,
        'meessage': serializer.data,
        'api-key': key_token,
        'WARNING': 'Do not show the api key to anyone'
    }, status=status.HTTP_201_CREATED)  


