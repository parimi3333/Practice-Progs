from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=70)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length=45)