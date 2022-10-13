from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"input.html")
def home1(request):
    return render(request,"input1.html")
def add(request):
    if request == 'post':
        x = int(request.POST['t2'])
        y = int(request.POST['t1'])
        z = x + y
        return HttpResponse('the add value is :'+str(z))
    else:
        x = int(request.GET['t1'])
        y = int(request.GET['t2'])
        z = x + y
        return HttpResponse('the add value is :'+str(z))