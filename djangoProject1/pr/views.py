from django.shortcuts import render
from django.views import View
from .forms import productapp
from django.http import HttpResponse
# Create your views here.
class input(View):
    def get(self,request):
        p=productapp()
        return render(request,"kj.html",{"hii":p})
class insert(View):
    def post(self,request):
        data=productapp(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("data submitted sucessfully")