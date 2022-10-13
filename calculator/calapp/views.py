from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"input1.html")


def calculate(request):
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        op = request.POST['operation']
        if op == '+':
                z = x + y
                return HttpResponse("the add "+str(z))
        elif op == '-':
                z = x - y
                return HttpResponse("the add " + str(z))
        elif op == '*':
                z = x * y
                return HttpResponse("the add " + str(z))
        elif op == '/':
                z = x / y
                return HttpResponse("the add " + str(z))
        elif op == '%':
                z = x % y
                return HttpResponse("the add " + str(z))



