from django.shortcuts import render
from .models import profile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def signup_form(request):
    return render(request,'signup.html')
def login_form(request):
    return render(request,'login.html')
def signup_attempt(request):
    usernameid=request.POST['un']
    emailid = request.POST['t2']
    passwordid = request.POST['t3']
    first_name = request.POST['t4']
    last_name = request.POST['t5']
    user = User.objects.create_user(username=usernameid,email=emailid,password=passwordid)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    profiel_obj = profile.objects.create(user = user)
    profiel_obj.save()
    return HttpResponse('completed')
def login1(request):
    x = request.POST['usern']
    y = request.POST['passw']
    user = authenticate(username=x,password=y)
    sample_instance = profile.objects.gets(user=x)
    value_of_name = sample_instance.is_verified
    if value_of_name == 'false':
        return HttpResponse('your acount is not verified please contact your higher autherity')
    elif user is not None:
        login(request,user)
        return render(request,'empd.html')
    else:
        return render(request,'login.html')
def logout1(request):
    logout(request)
    return render(request,'login.html')