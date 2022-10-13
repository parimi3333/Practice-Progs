from django.db import models

# Create your models here.
class Employe(models.Model):
    eid = models.IntegerField(primary_key=True)
    efirstname = models.CharField(max_length=60)
    elastname = models.CharField(max_length=60)
    esal = models.DecimalField(max_digits=20,decimal_places=2)
    ebranch = models.CharField(max_length=60)
    edepartment = models.CharField(max_length=60)
    eproject = models.CharField(max_length=60)