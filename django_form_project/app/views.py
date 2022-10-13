from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.
def input(request):
    p_f=productform
    return render(request,"input.html",{"product_form":p_f})
def submit(request):
    data_pf=productform(request.POST)
    if data_pf.is_valid():
        p=product(
            eid=data_pf.cleaned_data['eid'],
            name = data_pf.cleaned_data['name'],
            mfdt = data_pf.cleaned_data['mfdt'],
            expdt = data_pf.cleaned_data['expdt']
        )
        p.save()
    return HttpResponse('data submitted sucessfully')