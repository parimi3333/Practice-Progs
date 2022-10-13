from django import forms

class productform(forms.Form):
    pid=forms.IntegerField()
    pname=forms.CharField(max_length=20)
    pcost=forms.IntegerField()
    pmfdt=forms.DateField()
    pexpdt=forms.DateField()