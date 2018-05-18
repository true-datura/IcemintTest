from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


class BlogUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('blog_name', 'blog_description',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'blog_name',
                'blog_description',
            ),
        }),
    )


admin.site.register(User, BlogUserAdmin)
