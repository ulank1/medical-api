from django.contrib import admin

# Register your models here.
from post.models import Post, User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(Post, PostAdmin)