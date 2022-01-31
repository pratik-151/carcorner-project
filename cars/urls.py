from unicodedata import name
from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('',views.cars,name='cars'),
    path('car/<int:id>',views.car_details,name='car_details'),
    path('search/',views.search,name='search')
]