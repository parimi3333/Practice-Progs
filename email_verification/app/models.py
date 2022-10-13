from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    id = models.IntegerField(auto_created=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=60,default='pbgp')
    is_verified = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    auth_token = models.CharField(max_length=120)
    def __str__(self):
        return self.user.username


class employe(models.Model):
      empid = models.IntegerField(primary_key=True)
      empname = models.CharField(max_length=60)
      empsal = models.IntegerField()
      empbranch = models.CharField(max_length=45)
      emprole = models.CharField(max_length=45)