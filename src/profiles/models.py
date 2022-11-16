from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """ Custome user model """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    middle = models.CharField(max_length=100)
    first_login = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')


