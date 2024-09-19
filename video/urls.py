from os.path import pathsep
from django.urls import path
from . import views

urlpatterns=[
    path('vide', views.Video)
]
