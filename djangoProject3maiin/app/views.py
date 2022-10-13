import random

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from djangoProject3maiin import settings
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import profile,employe
# Create your views here.
def login_form(request):
    return render(request,'login.html')
def signup_form(request):
    return render(request,'signup.html')
def verify_ac(request):
    return render(request,'verify.html')

def signup_atempt(request):
    username = request.POST['un']
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['t4']
    last_name = request.POST['t5']
    token = random.randint(10000,99999)

    user = User.objects.create_user(username=username,email=email,password=password)
    user.auth_token = str(token)
    user.first_name = first_name
    user.last_name = last_name

    user.save()
    profile_obj = profile.objects.create(user=user)
    profile_obj.auth_token = str(token)
    profile_obj.is_verified = False
    profile_obj.username = username
    profile_obj.save()
    sending_mail(token)
    return render(request,'verify.html')
def sending_mail(request):
    subject = 'hai amma rey ela unnav'
    message = f"mail vachinda mama matladali oka sari {request}"
    from_mail = settings.EMAIL_HOST_USER
    to_list = ['balagangaprasanth.1997@gmail.com']
    send_mail(subject,message,from_mail,to_list)
    return True
def verify(request):
    otp = request.POST['otp']
    username = request.POST['username']
    obj = profile.objects.filter(user=username)
    ver = obj.auth_token
    if obj is not None:
        if otp == ver:
            obj.is_verified = True
            obj.save()
            return HttpResponse('your account is verified')
        else:
            return HttpResponse('otp is inavalid')
    else:
        return HttpResponse('please give valid credintials')
def login1(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    obj = profile.is_verified
    con = True
    if obj != con:
        return HttpResponse('your account is not confirmed yet please consult your superior')
    else:

        if user is not None:
            login(request, user)
            return render(request, 'empd.html')
        else:
            return render(request, 'login.html')
def logut1(request):
    logout(request)
    #return render(request,'login.html')
from django.shortcuts import render

# Create your views here.
