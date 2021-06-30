from os import name
from django import urls
from django.urls import path
from .views import home,form_pelicula,Ver,form_mod_pelicula


urlpatterns = [
    path('',home,name="home"),
    path('form_pelicula',form_pelicula,name='form_vehiculo'),
    path('ver',Ver,name="ver"),
    path('form_mod_pelicula/<id>',form_mod_pelicula,name="form_mod_pelicula")
]