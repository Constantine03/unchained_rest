from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer, TodoSerializer
from todos.models import Todo


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TodoAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

