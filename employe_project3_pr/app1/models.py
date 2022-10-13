from django.db import models

# Create your models here.

class employe(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class branch(models.Model):
    name = models.CharField(max_length=30)
    employes = models.ManyToManyField(employe,through='enrolement')
    def __str__(self):
        return self.name
class enrolement(models.Model):
    employe = models.ForeignKey(employe,on_delete=models.CASCADE)
    branch = models.ForeignKey(branch,on_delete=models.CASCADE)
