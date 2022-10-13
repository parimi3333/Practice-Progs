from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class post(View):
    def post(self,request):
        return render(request,'post.html')

class add(View):
    def add(self,request):
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        z = x + y
        return HttpResponse('the add val is:'+str(z))
