from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,"input.html")
def insert(request):
    x=int(request.POST['t1'])
    y=int(request.POST['t2'])
    z=x+y
    res=HttpResponse('data submitted sucessfully')
    res.set_cookie('z',z,max_age=60)
    return res
def display(request):
    if 'z' in request.COOKIES:
        SUM = request.COOKIES['z']
        return HttpResponse("the sum is"+SUM)
    else:
       return HttpResponse("please emter values")