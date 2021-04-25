from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .forms import *

from .models import *


menu = [
        {"title": "Главная", "url_name": "home"},
        {"title": "Музыка", "url_name": "music"},
        {"title": "Скачать", "url_name": "downloadapp"},
        ]

class HomePage(TemplateView):
    template_name = 'sounds/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context


class Music(TemplateView):
    template_name = 'sounds/music.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Музыка'
        return context


class Playlists(ListView):
    paginate_by = 3
    posts = Playlist
    template_name = 'sounds/playlists.html'
    context_object_name = 'collection'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Плейлисты'
        return context

    def get_queryset(self):
        return Playlist.objects.filter()


class DownloadApp(TemplateView):
    template_name = 'sounds/download_app.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Скачать приложение'
        return context


class TheSong(ListView):
    pass


class TheArtist(ListView):
    pass

class ThePlaylist(ListView):
    pass

class LoginPage(TemplateView):
    template_name = 'sounds/login_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Авторизация'
        return context


class RegisterUser(CreateView):
    form_class = UserCreationForm()
    template_name = 'sounds/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        return context
