from django.db import models

# Create your models here.
class employe(models.Model):
    id = models.IntegerField(primary_key=True)
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=20)
    es = models.DecimalField(max_digits=20,decimal_places=2)
    br = models.CharField(max_length=30)
    bd = models.DateField()
