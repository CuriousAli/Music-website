from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('music/', Music.as_view(), name='music'),
    path('download/', DownloadApp.as_view(), name='downloadapp'),
    path('pashalka/', TestLoggedin.as_view(), name='test_login'),
    path('the-song/<slug:slug>/', TheSong.as_view(), name='thesong'),
    path('', TheArtist.as_view(), name='theartist'),
    path('login/', LoginPage.as_view(), name='loginpage'),
    path('register/', RegisterUser.as_view(), name='registerpage'),
]