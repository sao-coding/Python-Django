from django.contrib import admin
from mysite import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("id","nickname", "message", "pub_time", "enabled")
    ordering = ("-pub_time",)

admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)