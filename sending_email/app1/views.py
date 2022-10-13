import uuid
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from .models import profile,employe

# Create your views here.
def signupform(request):
    return render(request,'signup.html')
def loginform(request):
    return render(request,'login.html')
def token_sent(request):
    return render(request,"token.html")
def register_atempt(request):
        username2 = request.POST["t1"]
        email = request.POST["t2"]
        password = request.POST["t3"]
        try:
              if User.objects.filter(username = username2).first():
                   messages.success("username already taken")
                   return render(request,'login.html')

              elif User.objects.filter(email = email).first():
                   messages.success("email already exist")
                   return render(request,"login.html")
              user_obj = User.objects.create(username=username2,email=email,password=password)
              user_obj.save()
              profile_obj = profile.objects.create(user = user_obj)
              profile_obj.save()
              return HttpResponse('email sent please check it')
        except Exception as e:
            print(e)
