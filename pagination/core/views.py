from django.shortcuts import render
from .models import Movies

# for pagination
from django.core.paginator import Paginator
# Create your views here.

def all_movies(request):
    movies = Movies.objects.all()
    
     # search
    movie_name = request.GET.get('movie_name')  # name here is the name of the input tag
    
    if movie_name != '' and movie_name is not None:
        movies = movies.filter(name__icontains = movie_name)  # name__icontains -- returns if certain words matches the search
    

    # pagination
    paginator = Paginator(movies, 3)   # Paginator(object, noOfObject in a single page) 
    page = request.GET.get('page')
    movies = paginator.get_page(page)     # fetch objects on the current page

   
    return render(request, 'core/index.html', context= {'movies': movies})
