from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
def inputform(request):
    st = schoolform()
    return render(request,'input.html',{'data':st})
def submitform(request):
    s_d = schoolform(request.POST)
    if s_d.is_valid():
        s_d.save()
        return HttpResponse('your data is submitted sucessfully')

def display(request):
    s_d = school.objects.all()
    return render(request,'display.html',{'data':s_d})