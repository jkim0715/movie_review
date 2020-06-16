from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Review, Comment
from movies.models import Movie
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer,ReviewListSerializer,CommentSerializer,CommentListSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    print('hello Reviews')
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
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
def createcomment(request,review_id):
    review = get_object_or_404(Review,title = review_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = request.user, review= review) # NOT NULL CONSTRAINT FAILED (ID가 없을 때)
        return Response(serializer.data)
    return ''

@api_view(['POST'])
def deletecomment(request, comment_id):
   comment = get_object_or_404(Comment, id = comment_id)
   comment.delete()
   return HttpResponse(status=200)

@api_view(['POST'])
def updatecomment(request, comment_id):
    comment = get_object_or_404(Comment, id= comment_id)
    if request.user == comment.user:
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user, comment = comment)
        return Response(serializer.data)
    else:

        return HttpResponse(status=403)


#Review CRUD

@api_view(['GET'])
def detail(request,review_id):
    review = Review.objects.all()
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
def createreview(request):
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user = request.user) # NOT NULL CONSTRAINT FAILED (ID가 없을 때)
        return Response(serializer.data)
    else:
        return HttpResponse(status=500)

@api_view(['POST'])
def deletereview(request, review_id):
    review = get_object_or_404(Review, id = review_id)
    if request.user == review.user:
       review.delete()
       return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)
    

@api_view(['POST'])
def updatereview(request, review_id):
    review = get_object_or_404(Review, id= review_id)
    if request.user == review.user:
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user, review = review)
        return Response(serializer.data)
    else:
        return HttpResponse(status=403)

@api_view(['POST'])
def likereview(request, review_id):
    review = get_object_or_404(Review,id=review_id)
    if review.like_user.filter(pk=request.user.id).exists():
        review.like_user.remove(request.user)
    else:
        review.like_user.add(request.user)
    return HttpResponse(status= 200)
    
@api_view(['POST'])
def likecomment(request, comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    if comment.like_user.filter(pk=request.user.id).exists():
        comment.like_user.remove(request.user)
    else:
        comment.like_user.add(request.user)
    return HttpResponse(status= 200)