from django.urls import path,include
from . import views
urlpatterns = [
  path('', views.index), #영화 리스트
  path('<int:movie_id>/', views.detail), #영화 디테일
  path('moviecomment/', views.moviecomment),
]
