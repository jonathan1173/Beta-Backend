from django.urls import path
from .views import ChallengeListCreateView, UserChallengeListCreateView

urlpatterns = [
    path('challenges/', ChallengeListCreateView.as_view(), name='challenge-list-create'),
    path('user-challenges/', UserChallengeListCreateView.as_view(), name='user-challenge-list-create'),
]
