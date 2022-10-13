from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status,viewsets
# Create your views here.
class studentviewset(viewsets.ViewSet):
    def list(self,request):
        queryset = student.objects.all()
        serializers = studentserializer(queryset,many=True)
        return Response(serializers.data)
    def retrieve(self,request,pk):
        id = pk
        if id is not None:
            queryset = student.objects.get(id=id)
            serializers = studentserializer(queryset)
            return Response(serializers.data)
    def update(self,requset,pk):
        id=pk
        queryset = student.objects.get(id=id)
        serializers = studentserializer(queryset,data=requset.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'complete data updated'})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        id = pk
        if id is not None:
            queryset = student.objects.get(id=id)
            queryset.delete()
            return Response({'msg':'delete'})
    def create(self,request):
        serializers = studentserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'complete data deleted'})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)