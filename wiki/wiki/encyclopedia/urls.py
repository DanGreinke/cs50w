from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.article, name="article"),
    path("random", views.random_page, name="random"),
    path("search", views.search, name="search")
]
