from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'pub_date', 'group',)
    search_fields = ('text',)
    list_filter = ('pub_date', 'group',)
    empty_value_display = '<empty>'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'post', 'author', 'created',)
    search_fields = ('text', 'author',)
    list_filter = ('created',)
    empty_value_display = '<empty>'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following',)
    search_fields = ('user', 'following',)
    empty_value_display = '<empty>'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    empty_value_display = '<empty>'
