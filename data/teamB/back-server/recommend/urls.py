from django.urls import path
from . import views

app_name = 'recommend'
urlpatterns = [
    path('random/', views.random_tmdb, name='random_tmdb'),
    path('optimize_ott/<str:username>/', views.optimize_ott, name='optimize_ott'),
]