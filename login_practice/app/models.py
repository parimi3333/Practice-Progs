from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    username = models.CharField(User,max_length=70)
    email = models.CharField(max_length=70)
    password = models.CharField(max_length=70)