from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('ott/', views.ott_list, name='ott_list'),  # ott 리스트 보내기
    path('tmdb/<str:initial>', views.tmdb_movie_list, name='tmdb_movie_list'), # initial 받아서, 해당하는 ott리스트 보내주기
    path('detail/<int:movie_id>/', views.movie_detail, name='movie_detail'), 
    path('detail/<int:movie_id>/ott/', views.movie_ott, name='movie_ott'),
    path('likes/<int:movie_id>/', views.likes, name='likes'), # 좋아요 기능

    # comment
    path('comment/<int:movie_id>/', views.comment_create, name="comment_create"),
    path('search/<str:query>/', views.search_movies, name='search_movies'),

    # mypage
    path('user_likes/<str:username>/', views.user_likes, name="user_likes"),
    path('user_offer/<str:username>/', views.user_offer, name="user_offer"),
    path('user_ott/<str:username>/', views.user_ott, name="user_ott")

]
