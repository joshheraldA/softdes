from django.db import models

class AdminUser(models.Model):
    """
    the admin user class that contains functionality that BaseUser class doesn't have

    Args:
        username (str): the name of admin user. Max length is set at 255
        password (str): the hashed password of admin user. Max length set at 255
        backup_password (str): Auto-generated admin password. Given after creating an account. WARNING: Do not release it to any website for security purposes
    """

    