from django.db import models

# Create your models here.
class employe(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=45)
    erole = models.CharField(max_length=45)
    edept = models.CharField(max_length=45)
    esal = models.IntegerField()
