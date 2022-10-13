from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class home(View):
    def get(self,request):
        return render(request,'input.html')
class add(View):
    def post(self,request):
        x = request.POST['t1']
        y = request.POST['t2']
        z = x + y
        return HttpResponse('the add val is:'+str(z))