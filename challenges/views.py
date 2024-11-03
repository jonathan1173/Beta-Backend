# challenges/views.py
from rest_framework import generics, permissions
from .models import Challenge
from .serializers import ChallengeSerializer, ChallengeDetailSerializer
from rest_framework.pagination import PageNumberPagination

# Clase de paginación personalizada
class ChallengePagination(PageNumberPagination):    
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# Vista para listar y crear desafíos
class ChallengeListCreateView(generics.ListCreateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    pagination_class = ChallengePagination
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

# Vista para obtener detalles de un desafío específico
class ChallengeDetailView(generics.RetrieveAPIView):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación
