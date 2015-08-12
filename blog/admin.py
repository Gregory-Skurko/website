from django.contrib import admin
from blog.forms import AdminUserChangeForm, AdminUserAddForm
from models import Post, Comment, Tag, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created')

class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserAddForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'email',
            'avatar',
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'avatar')}
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)



















