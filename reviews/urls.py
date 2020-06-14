from django.urls import path
from . import views
urlpatterns = [
  path('', views.index), #리뷰 리스트 
  path('comment/<int:review_id>' , views.comment_list),
  path('comment/detail/<int:comment_id>' , views.comment_detail), #영화 리뷰코멘트
  path('detail/<int:review_id>/', views.detail), #영화 리뷰 디테일
  path('create/<int:movie_id>/', views.createreview), #영화리뷰 만들기

]
