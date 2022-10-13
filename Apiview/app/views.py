from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

# Create your views here.
@api_view(['GET','POST'])
def home(request):
    student_obj = student.objects.all()
    serializer_obj = studentserializer(student_obj,many=True)
    return Response({'status':200,'message':'hai pbgp'})