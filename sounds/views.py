from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView

from .forms import *
from .models import *
from .utils import *


class HomePage(DataMixin, TemplateView):
    template_name = 'sounds/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class Music(DataMixin, TemplateView):
    template_name = 'sounds/music.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Музыка')
        return dict(list(context.items()) + list(c_def.items()))


class Surprise(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'sounds/surprise.html'
    context_object_name = 'playlist'
    login_url = '/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Плейлисты')
        return dict(list(context.items()) + list(c_def.items()))


class DownloadApp(DataMixin, TemplateView):
    template_name = 'sounds/download_app.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Скачать приложение')
        return dict(list(context.items()) + list(c_def.items()))


class TheSong(DataMixin, DetailView):
    model = Song
    template_name = 'sounds/thesong.html'
    context_object_name = 'tune'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Песня")
        return dict(list(context.items()) + list(c_def.items()))


class TheArtist(DataMixin, DetailView):
    pass


class LoginPage(DataMixin, TemplateView):
    template_name = 'sounds/login_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm()
    template_name = 'sounds/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
