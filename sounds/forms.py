from django import forms
from django.core.exceptions import ValidationError

from .models import *


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'



