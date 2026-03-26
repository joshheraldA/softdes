from .models import LeveledAPIKey
from rest_framework_api_key.permissions import BaseHasAPIKey

class UserAPIKey(BaseHasAPIKey):
    model = LeveledAPIKey

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        
        key = self.get_key(request)

        try:
            key_obj = LeveledAPIKey.objects.get_from_key(key)

            return key_obj.level == 'USER'

        except LeveledAPIKey.DoesNotExist:
            return False

class AdminAPIKey(BaseHasAPIKey):
    model = LeveledAPIKey

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        
        key = self.get_key(request)
        try:
            key_obj = LeveledAPIKey.objects.get_from_key(key)
            return key_obj.level in ['ADMIN']
        except LeveledAPIKey.DoesNotExist:
            return False
