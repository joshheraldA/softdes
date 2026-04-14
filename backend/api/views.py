from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from api.serializer import BaseUserSerializer

from api.model.user.baseuser import BaseUser
from api.model.leveledapikey import LeveledApiKey
from api.permission import AdminPermissions
from rest_framework_api_key.permissions import BaseHasAPIKey

from random import randint

class HasLeveledAPIKey(BaseHasAPIKey):
    model = LeveledApiKey

@api_view(['GET', 'POST'])
def view_user(request):
    serializer = BaseUserSerializer(data=request.data)

    numOfId = BaseUser.objects.values_list('idNum', flat=True)
    idRand = randint(10000, 99999)
    while idRand in numOfId:
        idRand = randint(10000, 99999)
    

    if serializer.is_valid():
        student = serializer.save(idNum=idRand)

        api_key_name = f'Key for joshheraldabelardo'
        api_key_instance, key_token = LeveledApiKey.objects.create_key(
            name=api_key_name,
            user=student,
            level='ADMIN'
        )

        return Response({
            'success': True,
            'data': serializer.data,
            'message': 'Save this and don\'t show it to ANYONE',
            'api_key': key_token
        }, status = status.HTTP_201_CREATED)
    else:
        return Response({
            'success': False,
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
