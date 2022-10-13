from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'get.html')
def postin(request):
    return render(request,"post.html")


def calculate(request):
    if request.method == "get":
        x = int(request.GeT['t1'])
        y = int(request.GET['t2'])
        z = x + y
        return HttpResponse('the add value is :' + str(z))
    else:
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        z = x + y
        return HttpResponse('the add value is :' + str(z))