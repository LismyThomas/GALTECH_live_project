from django.contrib import admin
from . models import UsersProfile,courses,Lessons,Video,Reviews
class Video_TabularInline(admin.TabularInline):
    model=Video

class lessons_admin(admin.ModelAdmin):
    inlines=[Video_TabularInline]  

admin.site.register(Lessons, lessons_admin)


# Register your models here.
admin.site.register(UsersProfile)
admin.site.register(courses)
admin.site.register(Video)
admin.site.register(Reviews)
