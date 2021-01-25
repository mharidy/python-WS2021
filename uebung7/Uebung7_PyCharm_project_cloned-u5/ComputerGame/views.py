from django.shortcuts import redirect, render
from .models import ComputerGame, Comment, Vote
from .forms import GameForm, CommentForm


def computer_games_list(request):
    all_games = ComputerGame.objects.all()
    context = {'all_games': all_games}
    return render(request, 'game-list.html', context)


def computer_game_details(request, **kwargs):
    computer_game_id = kwargs['pk']
    selected_game = ComputerGame.objects.get(id=computer_game_id)

    # Add comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.game = selected_game
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    comments = Comment.objects.filter(game=selected_game)
    comments_votes = Vote.objects.filter(game=selected_game)
    comments_with_votes = []
    for com in comments:
        up_votes = 0
        down_votes = 0
        for comment_vote in comments_votes:
            if comment_vote.up_or_down == "up" and comment_vote.comment_id == com.id:
                up_votes = up_votes + 1
            elif comment_vote.up_or_down == "down" and comment_vote.comment_id == com.id:
                down_votes = down_votes + 1
        comments_with_votes.append({'comment': com, 'up_votes': up_votes, 'down_votes': down_votes})

    context = {'that_game': selected_game,
               'comments_for_that_game': comments,
               'comment_form': CommentForm,
               'comments_with_votes': comments_with_votes}
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


def vote(request, pk: str, up_or_down: str, commentPK: int):
    game = ComputerGame.objects.get(id=int(pk))
    user = request.user
    comment = Comment.objects.get(id=commentPK)
    game.vote(user, up_or_down, comment)
    return redirect('game-detail', pk=pk)
