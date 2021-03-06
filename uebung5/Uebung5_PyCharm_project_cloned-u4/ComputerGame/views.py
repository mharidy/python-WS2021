from django.shortcuts import redirect, render
from .models import ComputerGame
from .forms import GameForm


def computer_games_list(request):
    all_games = ComputerGame.objects.all()
    context = {'all_games': all_games}
    return render(request, 'game-list.html', context)


def computer_game_details(request, **kwargs):
    print(kwargs)
    computer_game_id = kwargs['pk']
    selected_game = ComputerGame.objects.get(id=computer_game_id)
    context = {'that_game': selected_game}
    return render(request, 'game-detail.html', context)


def create_computer_game(request):
    if request.method == 'POST':
        form_in_my_function_based_view = GameForm(request.POST)
        form_in_my_function_based_view.instance.user = request.user
        if form_in_my_function_based_view.is_valid():
            form_in_my_function_based_view.save()
        else:
            pass
            print(form_in_my_function_based_view.errors)

        return redirect('games-list')

    else:  # request.method == 'GET'
        form_in_my_function_based_view = GameForm()
        print(form_in_my_function_based_view)
        context = {'form': form_in_my_function_based_view}
        return render(request, 'game-create.html', context)


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


def delete_game(request, **kwargs):
    computer_game_id = kwargs['pk']
    if request.method == 'POST':
        ComputerGame.objects.filter(id=computer_game_id).delete()
        all_games = ComputerGame.objects.all()
        context = {'all_games': all_games}
        return render(request, 'game-list.html', context)
    else:
        selected_game = ComputerGame.objects.get(id=computer_game_id)
        context = {'game': selected_game}
        return render(request, 'game-confirm-delete.html', context)
