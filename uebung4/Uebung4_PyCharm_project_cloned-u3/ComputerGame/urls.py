from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.ComputerGameListView.as_view(), name='games-list'),
    path('show/<int:pk>/', views.ComputergameDetailView.as_view(), name='game-detail'),
    path('add/', views.ComputergameCreateView.as_view(), name='game-create'),
    path('<pk>/delete/', views.ComputergameDeleteView.as_view(), name='game-confirm-delete'),


]
