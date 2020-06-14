from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings


from .serializers import MovieSerializer,MovieListSerializer , MovieCommentSerializer, GenreSerializer
from .models import Movie, MovieComment ,Genre
import requests
# Create your views here.




#1. API화면 -> api_view
#2. 사용자에게 응답을 해주는 도구 -> Response
@api_view(['GET'])
def index(request):
    paginator = PageNumberPagination()
    movies = Movie.objects.all()
    page = paginator.paginate_queryset(movies,request)
    serializer = MovieListSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



@api_view(['GET'])
def search(request,movie_title):
    if Movie.objects.filter(title=movie_title).exists():
        movie = Movie.objects.filter(title=movie_title)
        serializer = MovieSerializer(movie[0])
    else:
        url = f'https://api.themoviedb.org/3/search/movie?api_key=4aa6196c39a63ef5473aa8c1e096c329&language=ko-K&query={movie_title}'
        res = requests.get(url).json()
        movie_data = res.get("results")[0]
        if Movie.objects.filter(id=movie_data.get("id")).exists():
            movie = Movie.objects.filter(id=movie_data.get("id"))
            serializer = MovieSerializer(movie[0])
        else:
            genre = Genre()
            movie = Movie.objects.create(
                id=movie_data.get("id"),
                title=movie_data.get("title"),
                original_title=movie_data.get("original_title"),
                release_date=movie_data.get("release_date"),
                popularity=movie_data.get("popularity"),
                vote_count=movie_data.get("vote_count"),
                vote_average=movie_data.get("vote_average"),
                adult=movie_data.get("adult"),
                overview=movie_data.get("overview"),
                original_language=movie_data.get("original_language"),
                poster_path=movie_data.get("poster_path"),
                backdrop_path=movie_data.get("backdrop_path"),
            )
            movie.genres.set(movie_data.get("genre_ids"))
            movie.save()
            serializer = MovieSerializer(movie)
    return Response(serializer.data)
    
    
@api_view(['GET'])
def moviecomment(request,movie_title):
    moviecomment = MovieComment.objects.filter(title = movie_title)
    serializer = MovieCommentSerializer(moviecomment)
    return Response(serializer.data)

## 한줄평 작성 
# 로그인이 필요하구 
# 영화ID도 필요하네
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def createmoviecomment(request,movie_id):
    #  form data 로 보내야댐 
    movie = get_object_or_404(Movie,id = movie_id)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = request.user, movie= movie) # NOT NULL CONSTRAINT FAILED (ID가 없을 때)
        return Response(serializer.data)
    # print(serializer)
    return ''

# 장르데이터 받는거 
@api_view(['GET'])
def findgenre(request):
    genre = Genre.objects.all()
    serializer = GenreSerializer(genre,many=True)
    return Response(serializer.data)