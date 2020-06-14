from django.shortcuts import render,get_object_or_404
from .models import Review, Comment
from movies.models import Movie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer,ReviewListSerializer,CommentSerializer,CommentListSerializer
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
def comment_list(request, review_id):
    review = get_object_or_404(Review, id = review_id)
    comments = review.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    serializer = CommentSerializer(Comment)
    return Response(serializer.data)

@api_view(['POST'])
def createreview(request,movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = request.user, movie= movie) # NOT NULL CONSTRAINT FAILED (ID가 없을 때)
        return Response(serializer.data)
    return ''

@api_view(['POST'])
def createcomment(request,review_id):
    review = get_object_or_404(Review,title = review_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = request.user, review= review) # NOT NULL CONSTRAINT FAILED (ID가 없을 때)
        return Response(serializer.data)
    return ''