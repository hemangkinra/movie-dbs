from django.shortcuts import render, HttpResponseRedirect, redirect
from base.models import Movie, Actor, ActorMovie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializer, ActorSerializer, ActorMovieSerializer


@api_view(['GET'])
def home(request):
    context = ['content1', 'content2', 'content3']
    return Response(context)


@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        if q == 'srtt':
            movies = Movie.objects.all().order_by('title')
        elif q == 'srdt':
            movies = Movie.objects.all().order_by('-release_date')
        else:
            movies = Movie.objects.all()
        movieSe = MovieSerializer(movies, many=True)
        actors = []
        for movie in movies:
            actors.append(ActorMovieSerializer(
                ActorMovie.objects.filter(movie=movie), many=True).data)
        # print(type(movieSe.data))
        # print(type(actors))
        for a, m in zip(actors, movieSe.data):
            a.insert(0, m)
        return Response(actors)
    elif request.method == 'POST':
        some = request.data
        print("some  ", some['id'])
        movie = Movie.objects.get(id=int(some['id']))
        movie.upvote = some['upvote']
        movie.downvote = some['downvote']
        movie.save()
        # movie = MovieSerializer(data=request.data)
        # if movie.is_valid():
        #     movie.save()
        #     return Response(movie.data)
        # else:
        #     return Response(movie.errors)


@api_view(['GET'])
def actors(request):
    actors = Actor.objects.all()
    actorsSe = ActorSerializer(actors, many=True)
    movies = []
    for actor in actors:
        movies.append(ActorMovieSerializer(
            ActorMovie.objects.filter(actor=actor), many=True).data)
    for a, m in zip(actorsSe.data, movies):
        m.insert(0, a)
    return Response(movies)

# def votes(request, pk):
#     if request.method == 'POST':
#         movie = Movie.objects.get(id=pk)
#         if 'upvote' in request.POST:
#             movie.upvote += 1
#             movie.save()
#         elif 'downvote' in request.POST:
#             movie.downvote += 1
#             movie.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
