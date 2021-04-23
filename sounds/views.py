from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import *


menu = [
        {"title": "Главная", "url_name": "home"},
        {"title": "Музыка", "url_name": "music"},
        {"title": "Скачать", "url_name": "downloadapp"},
        {"title": "Плейлисты", "url_name": "playlists"},
        ]

class HomePage(ListView):
    model = Song
    template_name = 'sounds/index.html'
    extra_context = {'title': 'Главная страница'}


class Music(ListView):
    model = Song
    template_name = 'sounds/music.html'


class Playlists(ListView):
    paginate_by = 3
    posts = Playlist
    template_name = 'advertising/internet.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Реклама в интернете'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Playlist.objects.filter()


class DownloadApp(TemplateView):
    template_name = 'sounds/download_app.html'


class TheSong(ListView):
    pass


class TheArtist(ListView):
    pass

class ThePlaylist(ListView):
    pass

class LoginPage(TemplateView):
    template_name = 'sounds/login_page.html'
    extra_context = {'title': 'Авторизация'}

