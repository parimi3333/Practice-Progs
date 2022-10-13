from django import forms
from .models import product
class productapp(forms.ModelForm):
    class Meta:
        model = product
        fields = ['pid','pname','pcost']