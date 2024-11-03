from django.urls import path
from .views import UserListCreateView,IncrementPointsView,UserPointsView , UserRegisterView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('register/', UserRegisterView.as_view(), name='register'),
    
    path('userpoints/', UserPointsView.as_view(), name='user_points'),
    path('incrementpoints/', IncrementPointsView.as_view(), name='increment_points'),

]
