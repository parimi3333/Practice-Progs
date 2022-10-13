from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
    return render(request,"post.html")
def fun2(request):
    return render(request,"get.html")
def calculate(request):
        if request.method == 'GET':
                x = int(request.GET['t1'])
                y = int(request.GET['t2'])
                z = x + y
                return HttpResponse("the val is :" + str(z))
        else:
                x = int(request.POST['t1'])
                y = int(request.POST['t2'])
                z = x + y
                return HttpResponse("the val is :" + str(z))