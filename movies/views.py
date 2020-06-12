from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer,MovieListSerializer
from .models import Movie
# Create your views here.

#1. API화면 -> api_view
#2. 사용자에게 응답을 해주는 도구 -> Response
@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = request.user) # NOT NULL CONSTRAINT FAILED (ID가 없을 때)
        return Response(serializer.data)
    return ''
# 글 쓰는 사람 -> 장고 바깥 (Vue CLI)
# 글 쓰는 사람이, 글을 쓸 때 '내가 누구다!' 라는 정보를 함께 보낼 것. 'geunje', 'pwd123'
# Token이라는 것을 만들어서 보낼 것임.
#

@api_view(['GET'])
def detail(request,article_id):
    movie = get_object_or_404(Movie, pk=article_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)