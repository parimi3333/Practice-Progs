from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'input.html')
def inputform(request):
    x = int(request.POST['x'])
    y = int(request.POST['y'])
    z = x+y
    request.session['y']=z
    request.session.set_expiry(60)
    return HttpResponse('data submitted sucessfully')
def display(request):
    if request.session.has_key('y'):
        z = request.session['y']
        return HttpResponse(z)
    else:
        return HttpResponse('please enter values')