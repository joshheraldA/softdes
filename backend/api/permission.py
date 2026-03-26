from .models import LeveledAPIKey
from rest_framework_api_key.permissions import BaseHasAPIKey

class UserAndAdminAPIKey(BaseHasAPIKey):
    model = LeveledAPIKey

    def has_permission(self, request, view):
        # 1. First, let the library verify the key is real/active
        if not super().has_permission(request, view):
            return False
        
        # 2. Since it's valid, now check the role
        key = self.get_key(request)
        try:
            key_obj = LeveledAPIKey.objects.get_from_key(key)
            # 3. Use 'in' to allow both roles to pass this check
            return key_obj.level in ['USER', 'ADMIN']
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
