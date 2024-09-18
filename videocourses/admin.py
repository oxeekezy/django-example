from django.contrib import admin
from videocourses.models import Video


@admin.register(Video)
class AdminVideos(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
