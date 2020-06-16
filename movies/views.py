from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from django.http import HttpResponse

from .serializers import MovieSerializer,MovieListSerializer , MovieCommentSerializer, GenreSerializer
from .models import Movie, MovieComment ,Genre
import requests

import operator
from django.db.models import Q
from functools import reduce

from datetime import datetime
from django.db.models import Count
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
    else:# 이거 자료 없는거 뜨면 로직 자체가 멈춤 다음것도 왜인지 안된다?
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
def moviecomment(request,movie_id):
    moviecomment = MovieComment.objects.filter(movie_id=movie_id)
    serializer = MovieCommentSerializer(moviecomment,many=True)
    return Response(serializer.data)

## 한줄평 작성 
# 로그인이 필요하구 
# 영화ID도 필요하네
@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def createmoviecomment(request,movie_id):
    #  form data 로 보내야댐 
    movie = get_object_or_404(Movie,id = movie_id)
    # movie.vote_count +=1 이렇게 되나 
    #  좋아요도 movie.like user ? 이건 다른 테이블이라 이렇게 하면 안될거같은데? 
    temp = movie.moviecomment_set.filter(user=request.user)
    if temp:
        return HttpResponse(status=403)
    else:
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid():
            rate = int(request.data.get('rate'))
            movie.vote_count += 1
            movie.vote_average = (movie.vote_average*movie.vote_count +rate)/(movie.vote_count)
            movie.save()
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

# 선호장르
@api_view(['GET'])
def findmoviesbygenre(request):
    paginator = PageNumberPagination()
    arr = []
    for i in request.query_params:
        arr.append(request.query_params[i])
    movies = Movie.objects.filter(genres__in=arr).order_by('-vote_average').distinct()
    page = paginator.paginate_queryset(movies,request)
    serializer = MovieListSerializer(page, many=True)
    return paginator.get_paginated_response(serializer.data)

#영화 좋아요
@api_view(['POST'])
def like(request, movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    if movie.like_users.filter(pk=request.user.id).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return HttpResponse(status= 200)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_like_movies(request):
    print(request.user) 
    user = request.user
    movies = user.like_movies.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def add_movie(request,movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=4aa6196c39a63ef5473aa8c1e096c329&language=ko-Kr'
    movie_data = requests.get(url).json()
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
    tmp=(movie_data.get("genres"))
    tmp_list=[]
    for i in tmp:
        print(i)
        tmp_list.append(i['id'])

    movie.genres.set(tmp_list)
    # movie.genres.set(movie_data.get("genres").keys())
    movie.save()
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
  
def recommend(request):
    print(request.user)
    if len(request.user.like_movies.values('genres')) ==0 :
    ## 다른거 좋아요 누른 적 있으면 같은 장르.
        temp = datetime.now().second % 19
        arr= [10770,10752,10751,10749,10402,9648,878,99,80,53,37,36,35,28,27,18,16,14,12]
        genre = get_object_or_404(Genre, pk=arr[temp])
    else:
        genre_id = request.user.like_movies.values('genres').annotate(count=Count('genres'))[0].get('genres')
        genre = get_object_or_404(Genre, pk = genre_id)
    movies =Movie.objects.filter(genres=genre).order_by('-vote_average')[0:5]
    serializer = MovieSerializer(movies, many =True)
    return Response(serializer.data)