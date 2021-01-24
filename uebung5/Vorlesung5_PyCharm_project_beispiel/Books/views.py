from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .forms import BookForm
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'all_the_books'  # Default: object_list
    template_name = 'book-list.html'  # Default: book_list.html


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'that_one_book'  # Default: book
    template_name = 'book-detail.html'  # Default: book_detail.html


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book-create.html'  # Default: book_form.html
    success_url = reverse_lazy('book-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def book_list(request):
    context = {'all_the_books': Book.objects.all()}
    return render(request, 'book-list.html', context)
