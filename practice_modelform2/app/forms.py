from django import forms
from .models import school

class schoolform(forms.ModelForm):
    class Meta:
        model = school
        fields = ['roll_no','name','branch']