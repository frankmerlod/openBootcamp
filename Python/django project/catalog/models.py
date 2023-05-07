from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64, help_text='Nombre del genero')
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=64, help_text='Titulo de la pelicula')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    review = models.TextField(max_length=500, help_text='Resumen de la pelicula')
    duration = models.DurationField(help_text='Duracion de la pelicula')
    genre =models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Movie-detail', args=[str(self.id)])
    
class MovieInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico para esta pelicula')
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
        
    )
    
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad de la pelicula')
    
    class Meta:
        ordering = ['due_back']
        
    def __str__(self) -> str:
        return '%s, (%s)' % (self.id, self.movie.title)
    
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('author-details', args=[str(self.id)])
    
    def __str__(self):
        return '%s,%s' % (self.last_name, self.first_name)