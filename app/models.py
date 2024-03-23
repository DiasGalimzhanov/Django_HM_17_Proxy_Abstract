from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class DateHolder(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Post(DateHolder):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        
class Book(DateHolder):
    class Meta:
        verbose_name = 'Книга'  
        verbose_name_plural = 'Книги'

    class Genre(models.TextChoices):
        ADVENTURE = 'adventure', 'Приключения'
        ROMANCE = 'romance', 'Роман'
        FANTASY = 'fantasy', 'Фантастика'
        DETECTIVE = 'detective', 'Детектив'
        CLASSICAL = 'classical', 'Классика'
        HORROR = 'horror', 'Хоррор'
        BIOGRAPHY = 'biography', 'Биография'

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='books')
    genre = models.CharField(max_length=255, choices=Genre.choices)
    
    def __str__(self):
        return self.title
    
class ProxyBook(Book):
    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    def filter_by_genre(self, genre):
        return Book.objects.filter(genre=genre)
        
class ProxyPost(Post):
    class Meta:
        proxy = True
        
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk}) # http://127.0.0.1:8000/post/1
    

class Comment(DateHolder):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    
    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

