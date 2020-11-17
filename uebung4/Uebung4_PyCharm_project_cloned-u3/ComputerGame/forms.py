from django import forms
from .models import ComputerGame


class GameForm(forms.ModelForm):
    class Meta:
        model = ComputerGame
        fields = ['name', 'description', 'genre', 'added_on']
        widgets = {
            'genre': forms.Select(choices=ComputerGame.GAMES_TYPES),
            'user': forms.HiddenInput(),
        }
