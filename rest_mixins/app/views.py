from django.shortcuts import render
from .models import student
from .serializer import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,DestroyModelMixin,CreateModelMixin,UpdateModelMixin
# Create your views here.
class studentlist(GenericAPIView,ListModelMixin):
    queryset = student.objects.all()
    serializer_class = studentserializer
    def get(self,request):
        return self.list(request)
class studentcreate(GenericAPIView,CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = studentserializer
    def post(self,request):
        return self.create(request)
class studentup(GenericAPIView,UpdateModelMixin):
    queryset = student.objects.all()
    serializer_class = studentserializer

    def put(self, request,**kwargs):
        return self.update(request,**kwargs)
class studentrev(GenericAPIView, RetrieveModelMixin):
            queryset = student.objects.all()
            serializer_class = studentserializer

            def get(self, request, **kwargs):
                return self.retrieve(request, **kwargs)
class studentdelete(GenericAPIView,DestroyModelMixin):
        queryset = student.objects.all()
        serializer_class = studentserializer

        def delete(self, request, **kwargs):
            return self.destroy(request, **kwargs)