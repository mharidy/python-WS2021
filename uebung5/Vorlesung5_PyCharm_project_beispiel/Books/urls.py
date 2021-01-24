from django.urls import path
from . import views

urlpatterns = [
    #path('show/', views.BookListView.as_view(), name='book-list'),
    path('show/', views.book_list, name='book-list'),
    path('show/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('add/', views.BookCreateView.as_view(), name='book-create'),
]
