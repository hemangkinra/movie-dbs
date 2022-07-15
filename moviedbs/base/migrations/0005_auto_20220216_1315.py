# Generated by Django 4.0.2 on 2022-02-16 07:45

from django.db import migrations


def insertData(apps, schema_editor):
    Movie = apps.get_model('base', 'Movie')
    ActorMovie = apps.get_model('base', 'ActorMovie')
    Actor = apps.get_model('base', 'Actor')
    actor = Actor.objects.get(name="Emma Stone")
    movie = Movie.objects.get(title="Zombieland")
    user = ActorMovie(actor=actor, movie=movie)
    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220216_1306'),
    ]

    operations = [
        migrations.RunPython(insertData),
    ]
