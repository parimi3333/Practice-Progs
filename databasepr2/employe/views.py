from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import employe

# Create your views here.
class home(View):
    def get(self,request):
        return render(request,'home.html')
class insinput(View):
    def get(self,request):
        return render(request,"input.html")
class insert(View):
    def post(self,request):
        Id = int(request.POST['t1'])
        ename = request.POST['t2']
        elname = request.POST['t3']
        esal = request.POST['t4']
        ebranch = request.POST['t5']
        ebd = request.POST['t6']
        op = employe(id=Id,fn=ename,ln=elname,es=esal,br=ebranch,bd=ebd,)
        op.save()
        res = HttpResponse('data submitted sucessfully')
        return res
class display(View):
    def get(self,request):
        n = employe.objects.all()
        d = {"records":n}
        return render(request,"display.html",d)
class delete(View):
    def get(self,request):
        return render(request,"delete.html")
class deleteinput(View):
    def post(self,request):
        n = int(request.POST['t1'])
        d = employe.objects.get(id=n)
        d.delete()
        return render(request,"home.html")