from rest_framework_api_key.models import AbstractAPIKey
from django.db import models

from .user.baseuser import BaseUser
from .user.adminuser import AdminUser
class LeveledApiKey(AbstractAPIKey):
    """
    Extends AbstractAPIKey to include a permission level hierarchy.

    Levels:
        USER: Basic access level for standard users.
        ADMIN: Full access level for administrators.
        MODERATOR: Intermediate access level for moderators.

    Attributes:
        level (str): The permission level of the API key. Defaults to 'USER'.
        student (BaseUser): The user this API key belongs to. Optional.

    Example:
        >>> key = LeveledApiKey.objects.create(level='ADMIN', student=user)
        >>> key.level
        'ADMIN'
    """
    LEVEL_CHOICES = [
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
        ('MODERATOR', 'Moderator')
    ]

    user = models.ForeignKey(
        'BaseUser',
        on_delete=models.CASCADE,
        related_name='api_keys',
        null=True,
        blank=True
    )

    admin = models.ForeignKey(
        'AdminUser',
        on_delete=models.CASCADE,
        related_name='api_keys',
        blank=True,
        null=True
    )

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='USER')

