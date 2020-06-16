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
  path('getlikemovies/', views.get_like_movies), #좋아요 누른 영화들 가져오기 
  path('add_movie/<int:movie_id>/', views.add_movie), #영화 id 기준 영화 추가하기 
  path('recommend/', views.recommend),
]
