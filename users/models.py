from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

   """ Custome User Model """

   first_name = models.CharField(max_length=30,blank=True,default="Unnamed User")
   avatar = models.ImageField(upload_to="avatars", blank=True)
   superhost = models.BooleanField(default=False)
