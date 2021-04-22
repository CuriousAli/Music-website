from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class HomePage(ListView):
    pass


class SongsList(ListView):
    model = Song
    template_name = 'sounds/base.html'


class ArtistsList(ListView):
    pass


class Playlists(ListView):
    pass


class DownloadApp(ListView):
    pass


class TheSong(ListView):
    pass


class TheArtist(ListView):
    pass

class ThePlaylist(ListView):
    pass

class LoginPage(ListView):
    pass


