from django.db import models

# Create your models here.
class product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=30)
    pcost=models.IntegerField()