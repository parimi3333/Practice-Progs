"""rest_genaric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.studentlist.as_view()),
    path('cr',views.studentcreate.as_view()),
    path('rev/<int:pk>/',views.studentrev.as_view()),
    path('up/<int:pk>/',views.studenupdate.as_view()),
    path('de/<int:pk>/',views.studentdes.as_view()),
    path('lc',views.studenlc.as_view()),
    path('rud/<int:pk>/',views.studentrud.as_view())

]
