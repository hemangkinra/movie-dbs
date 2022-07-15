from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('movies/', views.movies),
    path('actors/', views.actors),
    # path('votes/<str:pk>/', views.votes),
]