from rest_framework import serializers
from .models import Review, Comment
from movies.serializers import MovieSerializer
from accounts.serializers import UserSerializer


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields =['id','title']


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields ="__all__"
        read_only_fields = ['id']

class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields =['id','title']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields ="__all__"
        read_only_fields = ['id']