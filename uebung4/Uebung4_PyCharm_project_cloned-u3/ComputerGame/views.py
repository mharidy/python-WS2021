from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .models import ComputerGame
from .forms import GameForm


class ComputerGameListView(ListView):
    model = ComputerGame
    context_object_name = 'all_games'  # Default: object_list
    template_name = 'game-list.html'  # Default: book_list.html


class ComputergameDetailView(DetailView):
    model = ComputerGame
    context_object_name = 'that_game'  # Default: book
    template_name = 'game-detail.html'  # Default: book_detail.html


class ComputergameCreateView(CreateView):
    model = ComputerGame
    form_class = GameForm
    template_name = 'game-create.html'  # Default: book_form.html
    success_url = reverse_lazy('games-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ComputergameDeleteView(DeleteView):
    model = ComputerGame
    context_object_name = "game"
    template_name = "game-confirm-delete.html"
    success_url = reverse_lazy('games-list')
