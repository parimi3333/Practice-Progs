from django.shortcuts import render
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def signup1(request):
    return render(request,'form_validation.html')
def login1(request):
    return render(request,'login.html')
def signup_form(request):
    username = request.POST['us']
    password = request.POST['p']
    user = User.objects.create_user(username=username,password=password)
    user.save()
    return render(request,'login.html')
def login_form(request):
    username = request.POST['us']
    password = request.POST['p']
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return render(request,'dummy.html')
def logout_form(request):
    logout(request)
    return render(request,'login.html')