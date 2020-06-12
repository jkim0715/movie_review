from django.test import TestCase
from bs4 import BeautifulSoup
import requests,pprint
import json

# url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=1144cdf8e1a2dab59dbca2112342e131&itemPerPage=30'
# response = requests.get(url).json()
# arr = response.get('movieListResult').get('movieList')
# pprint.pprint(arr)

# data = {}
# data ['key1'] = "keyinfo"
# data ['key2'] = "keyinfo2"

# 이런 식을 만들면 들어갈까? 컬럼명을 맞춰야 할거같은데 

#{{"movie_title" : }, {"movie_description": }, {"movie_genre":},{"movie_director":},} 

# movie_data= [{
#         "model": "movies.movie",
#         "pk": 1,
#         "fields": {
#             "title": "명량",
#             "description": "일본 멸 망",
#             "director": "재영",
#             "genre": "전쟁",
#             "rate": 10,
#         }
#     }]
# movie_dict ={}
# dict = {"member #002":{"first name": "John", "last name": "Doe", "age": 34},
#         "member #003":{"first name": "Elijah", "last name": "Baley", "age": 27},
#         "member #001":{"first name": "Jane", "last name": "Doe", "age": 42}}

# with open('data.json', 'w') as fp:
#     json.dump(movie_data, fp)



MOVIE_GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list?api_key=4aa6196c39a63ef5473aa8c1e096c329&language=ko-K'

#Genre 집어넣기 
# response = requests.get(MOVIE_GENRE_URL).json()
# genres = response["genres"]
# genre_arr = []
# for i in genres:
#     temp = {
#         "model": "movies.genre",
#         "pk": i.get("id"),
#         "fields": {
#             "name": i["name"],
#         }
#     }
#     genre_arr.append(temp)
# with open('genredata.json', 'w') as fp:
#     json.dump(genre_arr, fp)

#영화 싹다 집어 넣기
movie_list_arr=[]
for i in range(1001,1002):
    try:
        print(i)
        MOVIE_DISCOVER_URL = f'https://api.themoviedb.org/3/discover/movie?api_key=4aa6196c39a63ef5473aa8c1e096c329&language=ko-K&sort_by=popularity.desc&include_adult=false&include_video=false&page={i}'
        response_for_movie = requests.get(MOVIE_DISCOVER_URL).json()
        movies = response_for_movie.get('results')
        for movie in movies:
            temp = {
                "model": "movies.movie",
                "pk": movie["id"],
                "fields": {
                    'adult': movie['adult'],
                    'backdrop_path':  movie['backdrop_path'],
                    'genres':  movie['genre_ids'],
                    # 'id':  movie['id'],
                    'original_language':  movie['original_language'],
                    'original_title':  movie['original_title'],
                    'overview':  movie['overview'],
                    'popularity':  movie['popularity'],
                    'poster_path':  movie['poster_path'],
                    'release_date':  movie['release_date'],
                    'title':  movie['title'],
                    # 'video':  movie['video'],
                    'vote_average':  movie['vote_average'],
                    'vote_count':  movie['vote_count']
                }
            }
            movie_list_arr.append(temp)
    except:
        pass
with open('movies1.json', 'w') as fp:
    json.dump(movie_list_arr, fp)
print(len(movie_list_arr))
# arr1 =[]
# for idx, i in enumerate(arr):
#     temp = {
#         "model": "movies.movie",
#         "pk": idx,
#         "fields": {
#             "title": i["movieNm"],
#             "description": "일본 멸 망",
#             "director": i["directors"],
#             "genre": i["genreAlt"],
#             "rate": 10,
#         }
#     }
#     arr1.append(temp)
# print(arr1)