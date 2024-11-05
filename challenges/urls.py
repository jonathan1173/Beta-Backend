from django.urls import path
from .views import ChallengeListCreateView, ChallengeDetailView ,CodeTestView

urlpatterns = [
    path('challenges/', ChallengeListCreateView.as_view(), name='challenge-list-create'),
    path('challenges/<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),
    path('test-challenge/', CodeTestView.as_view(), name='test-challenge'),

]
