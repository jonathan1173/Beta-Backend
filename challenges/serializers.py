from rest_framework import serializers
from .models import Challenge, UserChallenge

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'difficulty', 'test', 'solution', 'category', 'language']

class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = ['id', 'user', 'challenge', 'progress', 'liked', 'disliked', 'comment']
