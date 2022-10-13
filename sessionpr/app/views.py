from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')
def insert(request):
    x=request.POST['t1']
    y=request.POST['t2']
    z=x+y
    request.session['z']=z
    request.session.set_expiry(60)
    return HttpResponse('data submitted sucessfully')
def display(request):
    if request.session.has_key('z'):
        z = request.session['z']
        return HttpResponse(z)
    else:
        return render(request,'input.html')
