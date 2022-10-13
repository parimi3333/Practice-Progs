from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signupform),
    path('login',views.loginform),
    path('tokensent',views.token_sent),
    path('register',views.register_atempt),
    path('send',views.send_mail)
]