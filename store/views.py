from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book, UserBook
from .serializers import BookSerializer, UserBookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserBookListCreateView(generics.ListCreateAPIView):
    queryset = UserBook.objects.all()
    serializer_class = UserBookSerializer
