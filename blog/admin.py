from django.contrib import admin
from models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)