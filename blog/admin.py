from django.contrib import admin
from django.contrib.auth.models import User
from models import Post, Comment, Tag, Avatar

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created')

class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'img')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Avatar, AvatarAdmin)