from .models import *

menu = [
    {"title": "Главная", "url_name": "home"},
    {"title": "Музыка", "url_name": "music"},
    {"title": "Скачать", "url_name": "downloadapp"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

