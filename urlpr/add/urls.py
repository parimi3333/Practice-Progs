from django.urls import path
from . import views
app_name='add'
urlpatterns=[
    path('home',views.home2)
]