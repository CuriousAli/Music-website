menu = [
        {"title": "Главная", "url_name": "home"},
        {"title": "Скачать", "url_name": "downloadapp"},
        {"title": "Зайди сюда", "url_name": "surprise"},
]

a_menu = [
        {"title": "Войти", "url_name": "account_login"},
        {"title": "Регистрация", "url_name": "account_signup"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        auth_menu = a_menu.copy()
        if self.request.user.is_authenticated:
            auth_menu.clear()
            auth_menu = [
                    {"title": "Выйти", "url_name": "account_logout"},
            ]

        context['menu'] = user_menu
        context['last_menu'] = auth_menu
        return context
