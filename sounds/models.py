import string
import random

from django.db import models
from django.urls import reverse
from django.utils.text import slugify



class Song(models.Model):
    """Треки"""
    name = models.CharField("Song", max_length=150, null=False)
    creator = models.ManyToManyField('Artist', related_name='songs')
    image = models.ImageField(upload_to="songs_images/%Y/%m/%d/", width_field=30, height_field=30, blank=True)
    album_of_song = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    video = models.URLField(default=None)
    genres = models.ManyToManyField('Genre', related_name='songs')
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('thesong', kwargs={'slug': self.slug})



    class Meta:
        ordering = ['name', 'is_published']
        verbose_name = "Песня"
        verbose_name_plural = "Песни"


class Artist(models.Model):
    """Исполнители"""
    name = models.CharField("Исполнитель", max_length=150, unique=True)
    albums = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(default=None)
    bio = models.TextField("Описание")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collection', kwargs={'collection_slug': self.slug})


    class Meta:
        ordering = ['name', ]
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Жанр", max_length=150, unique=True)
    description = models.TextField("Описание")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collection', kwargs={'collection_slug': self.slug})

    class Meta:
        ordering = ['name', ]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Album(models.Model):
    """Альбом содержащий треки"""
    name = models.CharField("Название альбома", max_length=150)
    creator = models.ForeignKey('Artist', on_delete=models.SET_DEFAULT, default=None)
    slug = models.SlugField(unique=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


    class Meta:
        ordering = ['name', ]
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"


