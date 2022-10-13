from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *


# Create your views here.
@api_view(['GET'])
def home(request):
    std = student.objects.all()
    serializer = studentserializer(std,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def post_list(request):
    std = student.objects.all()
    serializer = studentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updata_std(request,id):
    std = student.objects.get(id=id)
    serializer = studentserializer(instance=std,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_student(request,id):
    std = student.objects.get(id=id)
    std.delete()
    return Response('student is deleted')