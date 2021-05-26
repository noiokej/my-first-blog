from django.contrib import admin
from .models import Post, Comment
# Register your models here.


#admin.site.register(Post)
#admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'post', 'published_date')