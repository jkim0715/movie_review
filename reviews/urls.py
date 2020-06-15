from django.urls import path
from . import views
urlpatterns = [
  ## 영화 리뷰 http://localhost:8000/reviews/
  path('', views.index), #리뷰 리스트 
  path('detail/<int:review_id>/', views.detail), #영화 리뷰 디테일
  path('create/', views.createreview), #영화리뷰 만들기
  path('delete/<int:review_id>/', views.deletereview),
  path('like/<int:review_id>/', views.likereview), #커뮤니티 게시글 좋아요

  ## 영화 코멘트 http://localhost:8000/reviews/
  path('comment/<int:review_id>/' , views.comment_list), #리뷰에 딸려있는 코멘트 리스트 
  path('comment/detail/<int:comment_id>/' , views.comment_detail), #영화 리뷰코멘트
  path('comment/create/<int:review_id>/', views.createcomment), #영화 리뷰 코멘트 생성
  path('like/<int:comment_id>/', views.likecomment), # 커뮤니티 댓글 좋아요
]
