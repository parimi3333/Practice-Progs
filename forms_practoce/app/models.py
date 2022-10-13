from django.db import models

# Create your models here.
class employe(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    sal = models.DecimalField(max_digits=10,decimal_places=2)