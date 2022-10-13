from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.
@api_view(['POST','GET'])
def home(request):
    std = student.objects.all()
    serializer = studentserializer(std,many=True)
    return Response({'status':200,'payload':serializer.data})