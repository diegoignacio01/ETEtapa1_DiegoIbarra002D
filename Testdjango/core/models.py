from django.db import models

# Create your models here.
class Genero(models.Model):
    idGenero=models.IntegerField(primary_key=True,verbose_name='Id de Genero')
    nombreGenero=models.CharField(max_length=50,verbose_name='Nombre de Genero')

    def __str__(self):
        return self.nombreGenero

class Pelicula(models.Model):
    titulo=models.CharField(max_length=50,primary_key=True,verbose_name='Titulo de la pelicula')
    protagonista=models.CharField(max_length=50,verbose_name='Protagonista de la pelicula')
    sinopsis=models.CharField(max_length=300,verbose_name='Sinopsis de la pelicula')
    genero=models.ForeignKey(Genero,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    