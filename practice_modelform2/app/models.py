from django.db import models

# Create your models here.
class school(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    branch = models.CharField(max_length=70)