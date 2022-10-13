from django import forms

class productform(forms.Form):
    eid = forms.IntegerField()
    name = forms.CharField(max_length=70)
    mfdt = forms.DateField()
    expdt = forms.DateField()
