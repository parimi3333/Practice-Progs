from django.shortcuts import render
from django.contrib.auth.models import User
from .models import profile
import random
from django.contrib.auth import logout,login,authenticate
# Create your views here.
def signup_form(request):
    username = request.POST['un']
    email =request.POST['email']
    password = request.POST['password']
    first_name = request.POST['t4']
    last_name = request.POST['t5']
    auth_token = random.randint(10000,99999)
    user = User.objects.create_user(username=username,email=email,password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.auth_token = auth_token
    user.save()zzzzz
    profile_obj=profile.objects.