from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_article, name="add_article"),
    path("likearticle/<slug:id>/", views.like_article, name="like_article"),
    path("author/<slug:id>/", views.viewauthor, name="viewauthor")

]
