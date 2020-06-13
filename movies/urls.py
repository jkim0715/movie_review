from django.urls import path,include
from . import views

urlpatterns = [

  path('', views.index),
  path('<str:movie_title>/', views.search),
  path('detail/<int:movie_id>/', views.detail),
  path('moviecomment/<str:movie_title>/', views.moviecomment),

]
