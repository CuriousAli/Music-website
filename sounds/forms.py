from django import forms
from django.core.exceptions import ValidationError

from .models import *


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class PlaylistCreationForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 10:
            raise ValidationError('Слишком длинное название')
        return name