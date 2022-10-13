from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
class input(View):
    def get(self,request):
        return render(request,'input.html')

class insert(View):
    def post(self,request):
        fn=request.POST['Fn']
        ln=request.POST['Ln']
        us=request.POST['Un']
        eid=request.POST['eid']
        P=request.POST['P']
        user = User.objects.create_user (username=us,email=eid,password=P)
        user.First_name = fn
        user.Last_name = ln
        user.save
        messages.success(request,'your acount is created sucess fully')
        return redirect('login')
def login_user(request):
    if request.method=='POST':
        us=request.POST['Un']
        p=request.POST['P']
        user = authenticate(username=us,password=p)

        if user is not None:
            login(user)
        else:
            return render(request,'login.html')
