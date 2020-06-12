from django.shortcuts import render,get_object_or_404
from .models import Review, Comment
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer,ReviewListSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail(request,movie_id):
    review = get_object_or_404(Review, pk=movie_id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request,movie_id):
    review = get_object_or_404(Review, pk=movie_id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)