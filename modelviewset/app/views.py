from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class studentviewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]