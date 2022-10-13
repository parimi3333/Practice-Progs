from django.urls import path
from . import views
app_name = 'applicationurlsapp1'
urlpatterns = [
    path('input',views.input,name='input'),
    path('mul', views.mul, name='mul'),
]