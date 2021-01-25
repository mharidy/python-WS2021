from django import forms
from .models import Book, Comment


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'author', 'type', 'pages', 'date_published']
        widgets = {
            'type': forms.Select(choices=Book.BOOK_TYPES),
            'user': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'book': forms.HiddenInput(),
        }
