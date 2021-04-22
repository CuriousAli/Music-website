from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('songs/', SongsList.as_view(), name='songlist'),
    path('playlists/', Playlists.as_view(), name='playlists'),
    path('download/', DownloadApp.as_view(), name='downloadapp'),
    path('', TheSong.as_view(), name='thesong'),
    path('', TheArtist.as_view(), name='theartist'),
    path('', ArtistsList.as_view(), name='artistslist'),
    path('', ThePlaylist.as_view(), name='theplaylist'),
    path('', LoginPage.as_view(), name='loginpage'),
]