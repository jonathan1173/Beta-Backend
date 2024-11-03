# challenges/serializers.py

from rest_framework import serializers
from .models import Challenge, UserChallenge

# Serializador para listar desafíos
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'difficulty', 'category', 'language']

# Serializador para mostrar los detalles completos de un desafío
class ChallengeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'difficulty', 'test', 'solution', 'category', 'language']

# Serializador para el progreso del usuario en un desafío específico
class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = ['id', 'user', 'challenge', 'progress', 'liked', 'disliked', 'comment']
        read_only_fields = ['user', 'challenge']
