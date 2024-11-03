from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# En access/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User

class UserPointsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'points': user.points})

class IncrementPointsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        user.points += 1  # Incrementa los puntos en 1
        user.save()
        return Response({'points': user.points})


# register
# En access/views.py
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import User

class UserRegisterView(APIView):
    permission_classes = [AllowAny]  # Permitir acceso a todos los usuarios

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'El nombre de usuario ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)

        user = User(
            username=username,
            email=email,
            password=make_password(password)
        )
        user.save()
        return Response({'message': 'Usuario registrado exitosamente'}, status=status.HTTP_201_CREATED)
