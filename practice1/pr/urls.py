from django.urls import path
from . import views
from .views import insert
urlpatterns=[
    path('',views.input),
    path('insert',insert.as_view()),
    path('display',views.display),
]