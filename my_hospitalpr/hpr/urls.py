from django.urls import path
from .views import insert,input
urlpatterns=[
    path('',input.as_view()),
    path('register',insert.as_view())
]