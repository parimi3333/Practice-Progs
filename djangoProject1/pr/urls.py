from django.urls import path
from .views import input,insert
urlpatterns=[
    path('in',input.as_view()),
    path('insert',insert.as_view()),
]