from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Challenge, UserChallenge
from .serializers import ChallengeSerializer, UserChallengeSerializer

class ChallengeListCreateView(generics.ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class UserChallengeListCreateView(generics.ListCreateAPIView):
    queryset = UserChallenge.objects.all()
    serializer_class = UserChallengeSerializer
