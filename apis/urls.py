from django.urls import path

from .views import BookAPIView, TodoAPIView

urlpatterns = [
    path("", BookAPIView.as_view(), name="book_list"),
    path("todo/", TodoAPIView.as_view(), name="todo_list"),
]
