from django.urls import path
from . import views
app_name = 'applicationurlsapp'
urlpatterns = [
    path('input',views.input,name='input'),
    path('add', views.add, name='add'),
]