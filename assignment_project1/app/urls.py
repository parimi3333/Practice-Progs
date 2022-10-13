from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:user_name>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('follow/<str:user_name>', views.follow_user, name='follow'),
]