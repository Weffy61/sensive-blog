from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['tags', 'likes']
    readonly_fields = ['published_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author']
    list_display = ['post', 'author', 'text', 'published_at']
    readonly_fields = ['published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass



