from django.shortcuts import render
import requests, random
from django.views.decorators.http import require_safe
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from rest_framework import status

from rest_framework.response import Response

# permission Decorators
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import TmdbSerializer, OttSerializer, MovieSerializer, CommentSerializer, MovieDetailSerializer, SearchSerializer

from .models import Movie, Ott, Tmdb, Comment

# Create your views here.

# 1. ott filter button
# ott 명단 보내기
@api_view(['GET'])
def ott_list(request):
    ott_data = Ott.objects.all()
    serializer = OttSerializer(ott_data, many=True)
    # print('요청 보냄================')
    return Response(serializer.data)

# ott 버튼 누르면 해당 ott 영화 보내기
@api_view(['GET'])
def tmdb_movie_list(request, initial):

    # print("요청받음!!=============")
    # print(initial)
    tmdb_data = Tmdb.objects.all()
    # movie_data = Movie.objects.all()
    # print(movie_data)
    movie_list = []

    for movie in tmdb_data:
        m = movie.ott_lst
        
        if initial in m:  # ott 값이 포함된 경우
            rlt = movie.tmdb_id

            # print(rlt)
            movie_list.append(rlt)
    
    # print(movie_list)
    serializer = MovieSerializer(movie_list, many=True)

    return Response(serializer.data)


# movie_detail
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    print("detail 요청 받음")
    serializer = MovieDetailSerializer(movie)
    print(serializer.data)
    return Response(serializer.data)


# likes
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        print("좋아요 요청 받음")
        user = request.user
        
        if movie.like_users.filter(id=user.id).exists():
            # 이미 좋아요를 누른 경우, 좋아요 취소
            movie.like_users.remove(user)
            liked = False
            print(liked)
        else:
            # 좋아요를 누르지 않은 경우, 좋아요 추가
            movie.like_users.add(user)
            liked = True
            print(liked)

        # 좋아요 개수 업데이트
        likes_count = movie.like_users.count()
        movie.likes_count = likes_count
        movie.save()

        return Response({'liked': liked, 'likes_count': likes_count}, status=status.HTTP_201_CREATED)


# comments
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_id):
    print("댓글 받음")
    print(request.data)
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        print("댓글 조회 요청 들어옴")
        comments = Comment.objects.filter(movie=movie)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# search
@api_view(['GET'])
def search_movies(request, query):
    movies = Movie.objects.filter(title__icontains=query)

    movie_info = [{'id': movie.id, 'title': movie.title, 'poster_path': movie.poster_path} for movie in movies]
    # print(movie_info)

    serializer = SearchSerializer(movie_info, many=True)

    return Response(serializer.data)


# user가 좋아요 한 영화 리스트 보내기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_likes(request, username):
    print("좋아하는 영화 목록 요청 받음")
    user = request.user
    # print(user)
    liked_movies = user.like_movies.all()
    # print(liked_movies)

    serializer = MovieSerializer(liked_movies, many=True)
    return Response(serializer.data)

# user가 좋아요 한 영화랑 같은 영화 장르
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_offer(request, username):
    print("좋아하는 영화 기반 추천")
    user = request.user
    # print(user)
    liked_movies = user.like_movies.all()
    # print(liked_movies)

    # 장르가 같은 영화를 10개 가져옴
    genre_movies = []
    for movie in liked_movies:
        genre_movies.extend(Movie.objects.filter(genres__in=movie.genres.all()).exclude(pk=movie.pk)[:10])
    

    # 그 중에서 15개 랜덤으로 생성
    sorted_movies = sorted(genre_movies, key=lambda movie: movie.released_date, reverse=True)
    recommended_movies = []
    selected_ids = set()
    for movie in sorted_movies:
        if len(recommended_movies) == 15:
            break
        if movie.id not in selected_ids:
            recommended_movies.append(movie)
            selected_ids.add(movie.id)

    # 만약 추천할 영화가 15개보다 적다면 나머지 영화를 랜덤으로 추가
    remaining_count = 15 - len(recommended_movies)
    if remaining_count > 0:
        remaining_movies = list(set(sorted_movies) - selected_ids)
        random_movies = random.sample(remaining_movies, remaining_count)
        recommended_movies.extend(random_movies)

    serializer = MovieSerializer(recommended_movies, many=True)
    return Response(serializer.data)
