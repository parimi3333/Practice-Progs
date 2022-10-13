from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def studnetlist(request):
    student_obj = student.objects.all()
    serializer = studentserializer(student_obj,many=True)
    return Response(serializer.data)
#create
@api_view(['POST'])
def student_creat(request):
    #student_obj = student.objects.all()
    serializer = studentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def update_student(request,id):
    student_obj = student.objects.get(id=id)
    serializer = studentserializer(instance=student_obj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_student(request,id):
    delete_obj = student.objects.get(id=id)
    delete_obj.delete()
    return Response('book is deleted')