from django import forms
from .models import *

class employeform(forms.ModelForm):
    class Meta:
        model = employe
        fields = ['eid','name','sal']