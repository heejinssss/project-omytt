from django.shortcuts import render, get_object_or_404
from collections import Counter
from movies.models import Tmdb, Movie, Ott
from accounts.models import User
from movies.serializers import TmdbSerializer, MovieSerializer, OttSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404, get_list_or_404
import random
# Create your views here.

# 전체 영화 중 특정 영화 10개 선택해서 보내기
@api_view(['GET'])
def random_tmdb(request):
    movie_data = list(Movie.objects.all())

    # n개 랜덤으로 추출
    random_data = random.sample(movie_data, 10)
    # print(random_data)
    
    serializer = MovieSerializer(random_data, many=True)

    return Response(serializer.data)


# 최적의 ott 추천
# 내가 가지고 있는 ott는 제거하기
@api_view(['GET', 'POST'])
def optimize_ott(request, username):

    user = User.objects.get(username=username)  # username -> 이미 가지고 있는 ott는 제거
    print(user)
    # print('응답 받음!!')
    # print(request.data['payload'])
    print("user가 가지고 있는 ott")
    user_otts = user.ott_user.all()
    # print(user_otts.values())

    myotts = [] # user가 가지고 있는 ott 리스트 -> 제거하기

    for ott in user_otts.values():
        myotts.append(ott['id'])
    
    print(myotts)
    
    tmdb_ids = request.data['payload']  # 받은 tmdb_id 값
    ott_counts = [0] * 7  # 여기에 pk값으로 들어갈 것임

    otts = {
        "nfx" : 1,
        "wac" : 2,
        "wav" : 3,
        "ply" : 4,
        "apt" : 5,
        "dnp" : 6,
    }

    for tmdb_id in tmdb_ids:
        # print(tmdb_id)
        movie = get_object_or_404(Tmdb, pk=tmdb_id)
        # print(f'선택된 영화 {movie}')

        ott_lst = movie.ott_lst  # 그 영화의 ott_lst

        # 해당되는 ott의 pk값 찾기
        for ott_initial in ott_lst:
            ott_counts[otts.get(ott_initial)] += 1

    print(f'빼기 전 : {ott_counts}')

    # user가 가지고 있는 ott는 -1로 변경
    for i in myotts:
        ott_counts[i] = -1

    print(f'뺀 후 : {ott_counts}')
    rlt = ott_counts.index(max(ott_counts))  # 리스트에서 최댓값 인덱스 추출
    # print(f'rlt : {rlt}')
    final_recommend = Ott.objects.get(pk=(rlt))
    # print(final_recommend)
    
    serializer = OttSerializer(final_recommend)
    
    return Response(serializer.data)


