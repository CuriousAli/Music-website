from django.contrib import admin
from .models import *


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("id", "name",  "album_of_song", "is_published")
    list_display_links = ("name",)
    list_filter = ("genres", "is_published")
    search_fields = ("name", "creator__name")


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("id", "name")
    list_display_links = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("id", "name")
    list_display_links = ("name",)
    list_filter = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("id", "name", "creator", "release_date")
    list_display_links = ("name",)
    list_filter = ("release_date", "name")
    search_fields = ("name", "creator__name")

