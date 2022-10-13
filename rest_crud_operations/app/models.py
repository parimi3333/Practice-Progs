from django.db import models

# Create your models here.
class student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=70)
    branch = models.CharField(max_length=70)