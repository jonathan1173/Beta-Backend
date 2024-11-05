from rest_framework import serializers
from .models import Challenge, UserChallenge

# para listar desafíos
class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'difficulty', 'category', 'language']

# para mostrar los detalles completos de un desafío
class ChallengeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ['id', 'title', 'description', 'difficulty', 'test', 'solution', 'category', 'language']

# para el progreso del usuario en un desafío específico
class UserChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChallenge
        fields = ['id', 'user', 'challenge', 'progress', 'liked', 'disliked', 'comment']
        read_only_fields = ['user', 'challenge']

# para provar lo que son los test
class CodeTestSerializer(serializers.Serializer):
    test = serializers.CharField()
    solution = serializers.CharField()
