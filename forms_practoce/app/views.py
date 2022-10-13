from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.
def inputform(request):
    E_f = employeform
    return render(request,'input.html',{'employe_f':E_f})
def submitform(request):
    E_f = employeform(request.POST)
    if E_f.is_valid():
        e = employe(
            eid = E_f.cleaned_data['eid'],
            name = E_f.cleaned_data['name'],
            sal = E_f.cleaned_data['sal']
        )
        e.save()
    return HttpResponse('your data submitted')
def display(request):
    e = employe.objects.all()
    return render(request,'base.html',{'emp_d':e})