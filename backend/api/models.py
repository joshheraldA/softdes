from django.db import models
from rest_framework_api_key.models import AbstractAPIKey

class StudentUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    cesPoints = models.IntegerField(default=0)
    idNum = models.IntegerField(default=0)
    # blank - True: meaning that it can be left nothing
    

    def __str__(self):
        return self.username

class AdminUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gmail = models.EmailField(max_length=254)

    def __str__(self):
        return self.username

class LeveledAPIKey(AbstractAPIKey):
    LEVEL_CHOICES = [
        ('USER', 'User'),
        ('MODERATOR', 'Moderator'),
        ('ADMIN', 'Admin')
    ]

    student = models.ForeignKey(
        'StudentUser',
        on_delete = models.CASCADE,
        related_name = 'api_keys',
        null = True,
        blank = True
    )

    admin = models.ForeignKey(
        'AdminUser',
        on_delete = models.CASCADE,
        related_name = 'api_keys', 
        null = True,
        blank = True
    )

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='USER')


# Create your models here.
