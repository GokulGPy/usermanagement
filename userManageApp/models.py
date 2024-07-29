# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# class AuthUser(AbstractUser):
#     user_image = models.ImageField(upload_to='user_images/', null=True, blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
