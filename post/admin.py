from django.contrib import admin

from post.models import Poputka, Poputchik


# Register your models here.


class PoputkaAdmin(admin.ModelAdmin):
    class Meta:
        model = Poputka


admin.site.register(Poputka, PoputkaAdmin)


class PoputchikAdmin(admin.ModelAdmin):
    class Meta:
        model = Poputchik


admin.site.register(Poputchik, PoputchikAdmin)
