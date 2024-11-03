# challenges/urls.py
from django.urls import path
from .views import ChallengeListCreateView, ChallengeDetailView

urlpatterns = [
    path('challenges/', ChallengeListCreateView.as_view(), name='challenge-list-create'),
    path('challenges/<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),  # Ruta para un desafío específico
]
