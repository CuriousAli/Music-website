from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView

from .models import *
from .utils import *


class HomePage(DataMixin, TemplateView):
    template_name = 'sounds/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class SearchResult(DataMixin, ListView):
    model = Song
    template_name = 'sounds/search.html'
    paginate_by = 3
    context_object_name = 'looking_for'

    def get_queryset(self):
        return Song.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поиск')
        context['q'] = self.request.GET.get('q')
        return dict(list(context.items()) + list(c_def.items()))


class Surprise(LoginRequiredMixin, DataMixin, TemplateView):
    template_name = 'sounds/surprise.html'
    context_object_name = 'playlist'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Пасхалка')
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
    context_object_name = 'song'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Песня")
        return dict(list(context.items()) + list(c_def.items()))







