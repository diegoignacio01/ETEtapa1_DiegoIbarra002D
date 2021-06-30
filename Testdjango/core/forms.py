from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.db.models import fields
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Genero,Pelicula




class PeliculaForm(ModelForm):

    class Meta:
        model=Pelicula
        fields=['titulo','protagonista','sinopsis','genero']
        labels ={
            'titulo':'Ingrese el titulo de la pelicula',
            'protagonista':'Ingrese el protagonista de la pelicula',
            'sinopsis':'Ingrese la sinopsis de la pelicula',
            'genero':'seleccione el genero de la pelicula'
        }
        widgets= {
            'titulo':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'titulo de la pelicula',
                    'id':'titulo'
                }
            ),

            'protagonista':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'protagonista de la pelicula',
                    'id':'protagonista'
                }
            ),

            'sinopsis':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'sinopsis de la pelicula',
                    'id':'sinopsis'
                }
            ),
            'genero':forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Genero de la pelicula',
                    'id':'genero'
                }
            )


        }