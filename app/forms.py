from django.forms import ModelForm
from .models import Post, Comment, Book

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'image', 'genre']