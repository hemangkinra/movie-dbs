from rest_framework.serializers import ModelSerializer, RelatedField, CharField
from base.models import Movie, Actor, ActorMovie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ActorMovieSerializer(ModelSerializer):
    actor = CharField(source='actor.name')
    movie = CharField(source='movie.title')

    class Meta:
        model = ActorMovie
        fields = '__all__'
