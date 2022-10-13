from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,related_name='following',blank=True)
    bio = models.TextField(default='no bio')
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def profiles_post(self):
        pass
    def __str__(self):
        return str(self.user.username)