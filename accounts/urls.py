from unicodedata import name
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_view,name='logout'),
    path('dashboard',views.dashboard,name='dashboard')

]