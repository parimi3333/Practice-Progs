from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST','GET'])
def home(request):
    return Response({"status":200,'message':'hi pbgp'})