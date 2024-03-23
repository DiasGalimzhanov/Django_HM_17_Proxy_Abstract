from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Post, ProxyPost, Comment, Book, ProxyBook
from .forms import PostForm, CommentForm, BookForm

class ListPost(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'list.html'
    
    def get_queryset(self):
        return ProxyPost.objects.all()
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('list')
    template_name = "create.html"

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['commentForm'] = CommentForm()
        context['comments'] = Comment.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        content = request.POST.get('content')
        self.object = self.get_object()
        Comment.objects.create(content=content, content_object=self.object)
        return redirect(reverse('detail', kwargs={'pk': self.object.pk}))
    
    def form_valid(self, form):
        if form.is_valid():
            form.content_object = self.object
            form.save()
        return super().form_valid(form)
    
class ListBook(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'list_books.html'
    
    def get_queryset(self):
        selected_genre = self.request.GET.get('genre')
        if selected_genre:
            return self.filter_by_genre(selected_genre)
        else:
            return ProxyBook.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Book.objects.values_list('genre', flat=True).distinct()
        return context
    
    def filter_by_genre(self, genre):
        return Book.objects.filter(genre=genre)
    

class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['commentForm'] = CommentForm()
        context['comments'] = Comment.objects.all()
        return context
    
    def book(self, request, *args, **kwargs):
        content = request.POST.get('content')
        self.object = self.get_object()
        Comment.objects.create(content=content, content_object=self.object)
        return redirect(reverse('book_detail', kwargs={'pk': self.object.pk}))
    
    def form_valid(self, form):
        if form.is_valid():
            form.content_object = self.object
            form.save()
        return super().form_valid(form)
    
class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('list_books')
    template_name = "create_book.html"

    

    
    