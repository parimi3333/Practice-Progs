from django import forms

class employeform(forms.Form):
    eid = forms.IntegerField()
    name = forms.CharField()
    sal = forms.IntegerField()