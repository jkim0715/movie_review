from django.urls import path
from . import views
urlpatterns = [
  path('', views.index), #리뷰 리스트 
  path('detail/<int:review_id>', views.detail)
]
