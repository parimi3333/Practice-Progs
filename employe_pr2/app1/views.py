from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .models import employe
from employe_pr2 import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .tokens import genarate_token
# Create your views here.
def home(request):
    return render(request,'home.html')
def login_page(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def signup1(request):
    Username = request.POST['un']
    email_id = request.POST['eid']
    Password = request.POST['p']
    user = User.objects.create_user(username=Username,email=email_id,password=Password)
    user.is_active = False
    subject="request to login"
    message1="give access"+user.username
    from_email = settings.EMAIL_HOST_USER
    to_lsit = ["balagangaprasanth.1997@gmail.com"]
    send_mail(subject,message1,from_email,to_lsit,fail_silently = True)
    current_site = get_current_site(request)
    message = render_to_string('',{
        'name':user.username,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':genarate_token.make_token(user),
    })
    email=EmailMessage(
        message,
        settings.EMAIL_HOST_USER,
        ["balagangaprasanth.1997@gmail.com"],
    )
    email.fail_silently = True
    email.send()
    return render(request,'login.html')
def login1(request):
    x = request.POST['usern']
    y = request.POST['passw']
    user = authenticate(username=x,password=y)
    if user is not None:
        login(request,user)
        return render(request,'empd.html')
    else:
        return render(request,'login.html')
def logout1(request):
    logout(request)
    return render(request,'login.html')
def insert1(request):
    return render(request,'add.html')
def delete1(request):
    return render(request,'delet.html')
def update1(request):
    return render(request,'update.html')
def insert(request):
                p_id = int(request.POST['pid'])
                p_name = request.POST['name']
                p_role = request.POST['role']
                p_dept = request.POST['dept']
                p_sal = int(request.POST['sal'])
                p1 = employe(eid=p_id,ename=p_name,erole=p_role,edept=p_dept,esal=p_sal)
                p1.save()
                res = HttpResponse('data submitted sucessfully')
                return res
def display(request):
                n = employe.objects.all()
                dit = {"records":n}
                return render(request,"display.html",dit)

def delete(request):
        P_id=int(request.GET["t1"])
        prod=employe.objects.filter(eid=P_id)
        prod.delete()
        resp = HttpResponse("product deleted successfully")
        return resp
def update(request):
        P_id=int(request.POST["t1"])
        p_name = request.POST["t2"]
        p_role = request.POST["t3"]
        p_dept = request.POST["t4"]
        p_sal = int(request.POST["t5"])
        prod=employe.objects.get(eid=P_id)
        prod.ename=p_name
        prod.erole=p_role
        prod.edept=p_dept
        prod.esal=p_sal
        prod.save()
        resp = HttpResponse("product updated successfully")
        return resp
def activate(request,uid64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and genarate_token.check_token(user,token):
        user.is_active=True
        user.save()
        return render(request,'login.html')
    else:
        return render(request,'failed.html')
