from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class getinput1(View):
    def get(self,request):
        return render(request,'getinput1.html')
class postinput1(View):
    def post(self,request):
        return render(request,'postinput1.html')
class add(View):
    def get(self,request):
        x = int(request.GET['t1'])
        y = int(request.GET['t2'])
        z = x + y
        return HttpResponse('the add val is:'+str(z))

    def post(self,request):
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        z = x + y
        return HttpResponse('the add val is:'+str(z))