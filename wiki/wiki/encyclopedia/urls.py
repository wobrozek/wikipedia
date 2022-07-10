from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("wiki", views.wikiForm, name="wikiForm"),
    path("randomWiki", views.randomWiki, name="randomWiki")
]
