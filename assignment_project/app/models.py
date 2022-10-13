from django.db import models
from app2.models import profile
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(profile,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.body)[:30]
    class Meta:
        ordering = ('-created')