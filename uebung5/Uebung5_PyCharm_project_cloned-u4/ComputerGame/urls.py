from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.computer_games_list, name='games-list'),
    path('show/<int:pk>/', views.computer_game_details, name='game-detail'),
    path('add/', views.create_computer_game, name='game-create'),
    path('<pk>/delete/', views.ComputergameDeleteView.as_view(), name='game-confirm-delete'),

]
