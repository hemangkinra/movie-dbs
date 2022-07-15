from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Movie, Actor, ActorMovie
# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)


def movies(request):
    q = request.GET.get('q')
    if q == 'srtt':
        movies = Movie.objects.all().order_by('title')
    elif q == 'srdt':
        movies = Movie.objects.all().order_by('-release_date')
    else:
        movies = Movie.objects.all()
    actors = []
    for movie in movies:
        actors.append(ActorMovie.objects.filter(movie=movie))
    movies = zip(movies, actors)
    context = {'movies': movies}
    return render(request, 'movies.html', context)


def actors(request):
    actors = Actor.objects.all()
    movies = []
    for actor in actors:
        movies.append(ActorMovie.objects.filter(actor=actor))
    actors = zip(actors, movies)
    context = {'actors': actors}
    return render(request, 'actors.html', context)


def votes(request, pk):
    if request.method == 'POST':
        movie = Movie.objects.get(id=pk)
        if 'upvote' in request.POST:
            movie.upvote += 1
            movie.save()
        elif 'downvote' in request.POST:
            movie.downvote += 1
            movie.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
