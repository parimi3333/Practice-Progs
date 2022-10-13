from django.urls import path
from . import views
app_name='urlp'
urlpatterns=[
    path('home',views.home)
]
