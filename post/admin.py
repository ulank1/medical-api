from django.contrib import admin

from post.models import Poputka, User, Poputchik


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(User, UserAdmin)


class PoputkaAdmin(admin.ModelAdmin):
    class Meta:
        model = Poputka

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(Poputka, PoputkaAdmin)


class PoputchikAdmin(admin.ModelAdmin):
    class Meta:
        model = Poputchik

    readonly_fields = 'created_at updated_at'.split()


admin.site.register(Poputchik, PoputchikAdmin)
