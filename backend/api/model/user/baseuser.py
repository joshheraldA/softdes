from django.db import models

class BaseUser(models.Model):
    """
    the data for base user

    Attributes:
        username (str): The user's username. Maxed at 255
        password (str): The user's hashed password. Maxed at 255
        email (str): The user's email address
        idNum (int): The user's assigned id number. Defaulted at 0
        cesPoints (int): The user's individual CES points. Defaulted at 0
    """
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    idNum = models.CharField(max_length=255, default='XXXXXXXXXXXXXXXXXXXXX')
    cesPoints = models.IntegerField(default=0)



    def __str__(self):
        return self.username 