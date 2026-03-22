from rest_framework import serializers
from .models import StudentUser

class UserStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = '__all__'