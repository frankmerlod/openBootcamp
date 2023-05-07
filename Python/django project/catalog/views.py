from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    num_movies = Movie.objects.all().count()
    num_instances = MovieInstance.objects.all().count()
    availables = MovieInstance.objects.filter(status_exact='a').count()
    num_directors = Director.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={
            'num_movies': num_movies,
            'num_instances': num_instances,
            'availables': availables,
            'num_directors': num_directors
        }
    )