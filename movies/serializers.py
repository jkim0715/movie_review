from rest_framework import serializers
from .models import Movie, MovieComment
from accounts.serializers import UserSerializer
#게시글 목록
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =['id','title']


#게시글 상세정보
class MovieSerializer(serializers.ModelSerializer):
    #accounts에가서 만들어야 함
    user = UserSerializer(required=False) # is_valid()에서 유무 검증 pass
    class Meta:
        model = Movie
        fields ="__all__"
        read_only_fields = ['id']

class MovieCommentSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)
    user = UserSerializer(required=False) # is_valid()에서 유무 검증 pass
    class Meta:
        model = MovieComment
        fields =['id','title','rate','user']