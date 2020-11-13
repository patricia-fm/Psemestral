from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.registro, name="registro"),
    path('registro/<int:reg_id>', views.detalleRegistro, name="registro")    
]