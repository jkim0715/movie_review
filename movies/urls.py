from django.urls import path,include
from . import views

urlpatterns = [

  path('', views.index),
  path('<str:movie_title>/', views.detail),
  path('moviecomment/<str:movie_title>/', views.moviecomment),

]
