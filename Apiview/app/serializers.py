from rest_framework import serializers
from .models import student
class studentserializer(serializers.ModelSerializer):
    class meta:
        feilds : '__all'