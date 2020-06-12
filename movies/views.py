from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer,MovieListSerializer , MovieCommentSerializer
from .models import Movie, MovieComment
# Create your views here.

#1. API화면 -> api_view
#2. 사용자에게 응답을 해주는 도구 -> Response
@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request,movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def moviecomment(request):
    moviecomment = MovieComment.objects.all()
    serializer = MovieCommentSerializer(moviecomment)
    return Response(serializer.data)