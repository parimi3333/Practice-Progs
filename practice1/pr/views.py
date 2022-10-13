from django.shortcuts import render
from django.http import HttpResponse
from .forms import productapp
from .models import product
from django.views import View
# Create your views here.
def input(request):
    h=productapp()
    return render(request,"input.html",{"hai":h})
class insert(View):
    def post(self,request):
        data=productapp(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("data submitted sucessfully")
def display(request):
    data = product.objects.all()
    return render(request,'display.html',{'p':data})