from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='common/main.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main_pop/', views.main_pop, name='main_pop'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('preofile/<int:user_id>/', views.profile_pw, name='profile_pw'),
    path('produce/',views.produce,name='produce'),
]