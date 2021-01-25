from django import forms
from .models import ComputerGame, Comment


class GameForm(forms.ModelForm):
    class Meta:
        model = ComputerGame
        fields = ['name', 'description', 'genre', 'added_on']
        widgets = {
            'genre': forms.Select(choices=ComputerGame.GAMES_TYPES),
            'user': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'game': forms.HiddenInput(),
        }
