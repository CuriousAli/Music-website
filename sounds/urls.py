from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('result/', SearchResult.as_view(), name='searchres'),
    path('surprise/', Surprise.as_view(), name='surprise'),
    path('download/', DownloadApp.as_view(), name='downloadapp'),
    path('result/<slug:slug>/', TheSong.as_view(), name='detailpage'),
    ]