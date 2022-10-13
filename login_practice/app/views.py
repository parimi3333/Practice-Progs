from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.http import HttpResponse

# Create your views here.
def signupht(request):
    return render(request,'signup.html')
def login1(request):
    return render(request,'loginform.html')
def inputform(request):
    username = request.POST['us']
    email = request.POST['e']
    password = request.POST['ps']
    user = User.objects.create_user(username=username,email=email,password=password)
    user.save()
    return HttpResponse('registration sucessfull')
def loginform(request):
    username = request.POST['us']
    password = request.POST['p']
    z = authenticate(username=username,password=password)
    if z is not None:
        #request.session['g']=z
    #    request.session.set_expiry(60)
        login(request,z)
        return render(request,'home.html')
    else:
        return HttpResponse('please give valid credentials')
def logoutform(request):
   # if request.session.has_key('g'):
        logout(request)
        return render(request,'loginform.html')