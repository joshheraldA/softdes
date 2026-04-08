from .model.user.baseuser import BaseUser
from rest_framework import serializers

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'


