from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Book)
admin.site.register(Comment)
# Register your models here.