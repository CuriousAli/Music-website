from .models import *

menu = [
    {"title": "Главная", "url_name": "home"},
    {"title": "Музыка", "url_name": "music"},
    {"title": "Скачать", "url_name": "downloadapp"},
    {"title": "Зайди сюда", "url_name": "surprise"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)

        context['menu'] = user_menu
        return context

