from rest_framework import serializers
from .models import Review, Comment
from movies.serializers import MovieSerializer
from accounts.serializers import UserSerializer
from django.conf import settings

User = settings.AUTH_USER_MODEL
class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields =['id','title','user','created_at']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    like_user = serializers.PrimaryKeyRelatedField(queryset=UserSerializer, many=True, required=False)
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
    review = ReviewSerializer(required=False)
    like_user = serializers.PrimaryKeyRelatedField(queryset=UserSerializer, many=True, required=False)
    class Meta:
        model = Comment
        fields ="__all__"
        read_only_fields = ['id']