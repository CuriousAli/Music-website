from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('music/', Music.as_view(), name='music'),
    path('playlists/', Playlists.as_view(), name='playlists'),
    path('download/', DownloadApp.as_view(), name='downloadapp'),
    path('', TheSong.as_view(), name='thesong'),
    path('', TheArtist.as_view(), name='theartist'),
    path('', ThePlaylist.as_view(), name='theplaylist'),
    path('login/', LoginPage.as_view(), name='loginpage'),
    path('register/', RegisterUser.as_view(), name='registerpage'),
]