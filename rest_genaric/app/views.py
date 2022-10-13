from django.shortcuts import render
from .models import *
from .serializerss import *
from rest_framework.generics import ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView,CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
class studentlist(ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer
class studentcreate(CreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer
class studenupdate(UpdateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer
class studentrev(RetrieveAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer
class studentdes(DestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer
class studenlc(ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer
class studentrud(RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentserializer