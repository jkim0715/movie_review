from django.urls import path,include
from . import views

urlpatterns = [
  path('', views.index),
  path('like/<int:movie_id>/', views.like), #영화 좋아요 누르기 
  path('searchmovie/<str:movie_title>/', views.search), #영화 이름을 찾기
  path('searchmovies/genres/', views.findmoviesbygenre), #영화검색 by장르
  path('detail/<int:movie_id>/', views.detail), #영화 디테일 
  path('moviecomment/<int:movie_id>/', views.moviecomment), #영화 한줄평 리스트
  path('moviecomment/<int:movie_id>/create', views.createmoviecomment), #영화 한줄평 작성
  path('genre/',views.findgenre), #모든 영화장르 
]
