from django.db import models

class StudentUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    cesPoints = models.IntegerField(default=0)
    idNum = models.IntegerField(default=0)
    # blank - True: meaning that it can be left nothing
    

    def __str__(self):
        return self.username
    
# Create your models here.
