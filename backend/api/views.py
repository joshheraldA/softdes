from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserStudentSerializer
from .models import StudentUser
from random import randint
    

@api_view(['GET', 'POST'])
def view_user(request):
    # get requsts of student user account 
    if(request.method == 'GET'):
        studentUser = StudentUser.objects.all()
        data = UserStudentSerializer(studentUser, many=True).data
        return Response({
            'success': True,
            'data': data
        }, status = status.HTTP_200_OK)

    # post requests of student user account 
    # requires a username, password, email and CES points, which is defaulted to 0
    elif request.method == 'POST':
        serializer = UserStudentSerializer(data=request.data)

        numOfId = StudentUser.objects.values_list('idNum', flat=True)
        idRand = randint(10000, 99999)
        while idRand in numOfId:
            idRand = randint(10000, 99999)
        

        if(serializer.is_valid()):
            serializer.save(idNum=idRand)
            return Response({
                'success': True,
                'data': serializer.data,
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                'success': False,
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def put_user(request, idNum):
    try:
        studentInstance = StudentUser.objects.get(idNum=idNum)
    except StudentUser.DoesNotExist:
        return Response({
            'success': False,
            'data': 'instance is not found'
        }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserStudentSerializer(studentInstance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'success': False,
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, idNum):
    try:
        instanceStudent = StudentUser.objects.get(idNum=idNum)
    except StudentUser.DoesNotExist:
        return Response({
            'success': True,
            'data': 'could not find instance'
        }, status=status.HTTP_404_NOT_FOUND)

    instanceStudent.delete()

    data = UserStudentSerializer(StudentUser.objects.all(), many=True).data
    return Response({
        'success': True,
        'data': data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def filter_user(request):
    nameData = request.GET.get('name')
    cesData = request.GET.get('cesp', 0)
    if cesData:
        data = StudentUser.objects.filter(
            cesPoints__gte=cesData,
            username__icontains=nameData
        )

        result = UserStudentSerializer(data, many=True).data

        return Response({
            'success': True,
            'data': result
        })

    elif nameData:
        data = StudentUser.objects.filter(username=nameData)

        result = UserStudentSerializer(data, many=True).data

        return Response({
            'success': True,
            'data': result
        }, status=status.HTTP_200_OK)

    else:
        return Response({
            'success': False,
            'data': 'need to input name'
        }, status=status.HTTP_400_BAD_REQUEST)

