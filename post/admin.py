from django.contrib import admin
from .models import Post,Job,Appointment,Schedule


# Register your models here.


class JobAdmin(admin.ModelAdmin):
    class Meta:
        model = Job

    readonly_fields = 'created_at updated_at'.split()
    list_display = 'job'.split()

admin.site.register(Job, JobAdmin)


class AppointmentInline(admin.StackedInline):
    model = Appointment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

    fields = 'job name surname experience'.split()
    readonly_fields = 'created_at updated_at'.split()
    list_display = 'name surname'.split()
    inlines = [AppointmentInline]

admin.site.register(Post, PostAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    class Meta:
        model = Schedule

    readonly_fields = 'created_at updated_at'.split()

admin.site.register(Schedule, ScheduleAdmin)




