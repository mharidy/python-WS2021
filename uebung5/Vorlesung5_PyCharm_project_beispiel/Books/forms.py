from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'author', 'type', 'pages', 'date_published']
        widgets = {
            'type': forms.Select(choices=Book.BOOK_TYPES),
            'user': forms.HiddenInput(),
        }
