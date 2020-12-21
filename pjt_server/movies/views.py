from django.shortcuts import get_object_or_404, render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer, MovieCommentSerializer, GetMovieCommentSerializer, ReviewSerializer, ReviewCommentSerializer, GetReviewSerializer, GetReviewCommentSerializer
from .models import Movie, MovieComment, Review, ReviewComment


def hello(request):
    return render(request, 'hello.html')


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movies_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def list_create_movie_comment(request, movie_pk):
    if request.method == 'GET':
        comments = MovieComment.objects.filter(movie=movie_pk)
        serializer = GetMovieCommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_movie_comment(request, comment_pk):
    comment = get_object_or_404(MovieComment, pk=comment_pk)

    if not request.user.movie_comments.filter(pk=comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'})
    comment.delete()
    return Response({ 'id': comment_pk })


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def list_create_movie_review(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_pk)
        serializer = GetReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_delete_movie_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'DELETE':
        if not request.user.user_reviews.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'})
        review.delete()
        return Response({ 'id': review_pk })
    else:
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def select_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.users_playlist.filter(pk=request.user.pk).exists():
        movie.users_playlist.remove(request.user)
    else:
        movie.users_playlist.add(request.user)
    return Response(status=status.HTTP_201_CREATED)



@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def list_create_review_comment(request, review_pk):
    if request.method == 'GET':
        comments = ReviewComment.objects.filter(review=review_pk)
        serializer = GetReviewCommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_review_comment(request, review_comment_pk):
    print(review_comment_pk)
    comment = get_object_or_404(ReviewComment, pk=review_comment_pk)

    if not request.user.review_comments.filter(pk=review_comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'})
    comment.delete()
    return Response({ 'id': review_comment_pk })