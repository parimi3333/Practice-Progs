from django.shortcuts import render
from .models import Employe
from django.http import HttpResponse
from django.views import View

# Create your views here.
def firstt(re):
    return render(re,'first.html')
class home(View):
        def get(self,request):
                return render(request,'home.html')
class input(View):
    def get(self,request):
        return render(request,"input.html")

class insert(View):
        def post(self,request):
                e_id = request.POST['t1']
                e_firstname = request.POST['t2']
                e_lastname = request.POST['t3']
                e_salary = request.POST['t4']
                e_branch = request.POST['t5']
                e_department = request.POST['t6']
                e_project = request.POST['t7']
                E = Employe(eid=e_id,efirstname=e_firstname,elastname=e_lastname,esal=e_salary,ebranch=e_branch,edepartment=e_department,eproject=e_project)
                E.save()
                res = HttpResponse('data submitted sucessfully')
                return res
class display(View):
        def get(self,request):
                n = Employe.objects.all()
                dit = {"records":n}
                return render(request,"display.html",dit)
class DeleteInputView(View):
    def get(self,request):
        return render(request,"delete.html")
class DeleteView(View):
    def get(self,request):
        e_id=int(request.GET["t1"])
        emp=Employe.objects.filter(eid=e_id)
        emp.delete()
        resp = HttpResponse("product deleted successfully")
        return resp
class UpdateInputView(View):
    def get(self,request):
        return render(request,"update.html")
class UpdateView(View):
    def post(self,request):
        e_id=int(request.POST["t1"])
        e_firstname = request.POST["t2"]
        e_lastname = request.POST['t3']
        e_sal = float(request.POST["t4"])
        e_branch = request.POST['t5']
        e_department = request.POST["t6"]
        e_project = request.POST["t7"]
        emp=Employe.objects.get(eid=e_id)
        emp.efirstname = e_firstname
        emp.elastname = e_lastname
        emp.esal = e_sal
        emp.ebranch = e_branch
        emp.edepartment = e_department
        emp.eproject = e_project
        emp.save()
        resp = HttpResponse("product updated successfully")
        return resp
