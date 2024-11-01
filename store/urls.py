from django.urls import path
from .views import BookListCreateView, UserBookListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('user-books/', UserBookListCreateView.as_view(), name='user-book-list-create'),
]
