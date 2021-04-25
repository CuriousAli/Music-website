from django import forms
from .models import *


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
