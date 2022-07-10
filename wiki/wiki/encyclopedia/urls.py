from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("wiki", views.wikiForm, name="wikiForm"),
    path("randomWiki", views.randomWiki, name="randomWiki"),
    path("addPage", views.addPage, name="addPage"),
    path("addPage/addForm", views.addForm, name="addForm")
]
