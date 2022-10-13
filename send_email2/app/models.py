from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.user.username
class employe(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=60)
    join_date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=45,default='it solutions')
    empsal = models.DecimalField(max_digits=10,decimal_places=2)
    empbranch = models.CharField(max_length=45)
    emprole = models.CharField(max_length=45)