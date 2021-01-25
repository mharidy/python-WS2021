from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .forms import BookForm, CommentForm
from .models import Book, Comment


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


def book_detail(request, **kwargs):
    book_id = kwargs['pk']
    book = Book.objects.get(id=book_id)

    # Add comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.book = book
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    comments = Comment.objects.filter(book=book)
    context = {'that_one_book': book,
               'comments_for_that_one_book': comments,
               'upvotes': book.get_upvotes_count(),
               'downvotes': book.get_downvotes_count(),
               'comment_form': CommentForm}
    return render(request, 'book-detail.html', context)


def vote(request, pk: str, up_or_down: str):
    book = Book.objects.get(id=int(pk))
    user = request.user
    book.vote(user, up_or_down)
    return redirect('book-detail', pk=pk)
