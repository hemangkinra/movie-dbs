from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)