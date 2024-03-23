from django.urls import path
from .views import ListPost, PostCreateView, PostDetailView, BookDetail, BookCreate, ListBook

urlpatterns = [
    path('', ListPost.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('book/', ListBook.as_view(), name='list_books'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),

    path('book/create/', BookCreate.as_view(), name='create_book'),
]
