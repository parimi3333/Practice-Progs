from django.db import models

# Create your models here.
class product(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    mfdt = models.DateField()
    expdt = models.DateField()