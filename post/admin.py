from django.contrib import admin
from post.models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(Post,PostAdmin)
