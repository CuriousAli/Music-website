from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('search/', SearchResult.as_view(), name='search'),
    path('surprise/', cache_page(3600)(Surprise.as_view()), name='surprise'),
    path('download/', cache_page(3600)(DownloadApp.as_view()), name='downloadapp'),
    path('song/<slug:slug>/', cache_page(60)(TheSong.as_view()), name='detailpage'),
]