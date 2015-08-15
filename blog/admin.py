from django.contrib import admin
from blog.forms import AdminUserChangeForm, AdminUserAddForm
from models import Post, Comment, Tag, User, Rating
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_view', 'title', 'visible', 'created')

    def user_view(self, obj):
        return obj.user

    user_view.short_description = 'Whose'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user_view', 'created')

    def user_view(self, obj):
        return obj.user

    user_view.short_description = 'Whose'

class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserAddForm

    list_display = ('username', 'email', 'last_login', 'date_joined',)
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
            'fields': ('username', 'email', 'password', 'avatar')}
         ),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Rating)
