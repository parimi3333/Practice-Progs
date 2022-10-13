from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse


# Create your views here.
def input(request):
    e_f = employeform()
    return render(request,'input.html',{'emp_d':e_f})
def submitform(request):
    e_f = employeform(request.POST)
    if e_f.is_valid():
        e_f.save()
        return HttpResponse('data submitted sucessfully')
def display(request):
    d = employe.objects.all()
    return render(request,'display.html',{'dis':d})