from rest_framework_api_key.permissions import BaseHasAPIKey
from .model.leveledapikey import LeveledApiKey
class BasePermissions(BaseHasAPIKey):
    """
        Functions:
            has_permission (request, view): Checks the permittable level users 
        
        Levels: 
            User
            Modrator
            Admim
    """

    model = LeveledApiKey

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
     
        key = self.get_key(request)
        try:
            key_obj = LeveledApiKey.objects.get_from_key(key)
            return key_obj.level in ['USER', 'ADMIN', 'MODERATOR']
        except LeveledApiKey.DoesNotExist:
            return False
    
class AdminPermissions(BaseHasAPIKey):
    """
        Functions:
            has_permission (request, view): Checks the permittable level users 
        
        Levels: 
            Admin
    """
    model = LeveledApiKey

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        key = self.get_key(request)

        try: 
            key_obj = LeveledApiKey.objects.get_from_key(key)
            return key_obj.level in ['ADMIN']
        except LeveledApiKey.DoesNotExist:
            return False
        
    