from django.contrib import admin
from .models import Post, Comment, HashTag

# Register your models here.
admin.site.register(Post)  # admin page등록
admin.site.register(Comment)
admin.site.register(HashTag)