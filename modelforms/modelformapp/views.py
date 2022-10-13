from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
# Create your views here.
from django.views import View


class Input(View):
    def get(self, request):
        p_f = ProductForm()
        return render(request, 'input.html', {"form_product": p_f})


class Insert(View):
    def post(self, request):
        data_product_form = ProductForm(request.POST)
        if data_product_form.is_valid():
            data_product_form.save()
            return HttpResponse("data inserted successfully")


# Create your views here.
