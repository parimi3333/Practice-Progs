from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login1',views.login_page),
    path('signup',views.signup),
    path('signup1',views.signup1),
    path('login',views.login1),
    path('logout',views.logout1),
    path('insert1',views.insert1),
    path('insert',views.insert),
    path('delete1',views.delete1),
    path('delete',views.delete),
    path('update1',views.update1),
    path('update',views.update),
    path('display',views.display),
    path('activate/<uid64>/<token>',views.activate),

]