from django.contrib import admin
from django.urls import path,include
from .views import *
name_app='administrador'

urlpatterns = [
    path('adm/',home_adm,name='admin'),

]