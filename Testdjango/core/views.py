from django.shortcuts import redirect, render
from .models import Pelicula
from .forms import PeliculaForm
# Create your views here.

def home(request):
    peliculas= Pelicula.objects.all()


    return render(request,'home.html',context={'datos':peliculas},
    
)

def form_pelicula(request):
    if request.method=='POST':
        pelicula_form=PeliculaForm(request.POST)
        if pelicula_form.is_valid():
            pelicula_form.save()
            return redirect('home')
    else:
        pelicula_form=PeliculaForm()
    return render(request,'core/form_crearpelicula.html',{'pelicula_form':pelicula_form})


def Ver(request):
    peliculas = Pelicula.objects.all()

    return render(request, 'core/ver.html', context={'peliculas':peliculas})


def form_mod_pelicula(request,id):
    pelicula = Pelicula.objects.get(titulo=id)

    datos ={
        'form': PeliculaForm(instance=pelicula)
    }
    if request.method == 'POST': 
        formulario = PeliculaForm(data=request.POST, instance = pelicula)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_mod_pelicula.html', datos)
