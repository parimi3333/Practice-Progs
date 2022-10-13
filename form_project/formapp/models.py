from django.db import models

# Create your models here.
class produtapp(models.Model):
    pid=models.IntegerField(primary_key=True,unique='pid')
    pname=models.CharField(max_length=20)
    pcost=models.IntegerField()
    pmfdt=models.DateField()
    pexpdt=models.DateField()

