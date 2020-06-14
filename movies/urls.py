from django.urls import path,include
from . import views

urlpatterns = [

  path('', views.index),
  path('searchmovie/<str:movie_title>/', views.search),
  path('detail/<int:movie_id>/', views.detail),
  path('moviecomment/<int:movie_id>/', views.moviecomment),
  path('moviecomment/<int:movie_id>/create', views.createmoviecomment),
  path('genre/',views.findgenre),
]
