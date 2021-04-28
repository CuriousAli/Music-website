from .models import *

menu = [
    {"title": "Главная", "url_name": "home"},
    {"title": "Скачать", "url_name": "downloadapp"},
    {"title": "Тест поле", "url_name": "test_login"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        return context

