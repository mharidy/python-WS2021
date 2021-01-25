from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.computer_games_list, name='games-list'),
    path('show/<int:pk>/', views.computer_game_details, name='game-detail'),
    path('add/', views.create_computer_game, name='game-create'),
    path('<pk>/delete/', views.delete_game, name='game-confirm-delete'),
    path('show/<int:pk>/vote/<str:up_or_down>/comment/<int:commentPK>', views.vote, name='game-vote'),

]
