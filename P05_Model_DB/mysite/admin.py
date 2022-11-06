from django.contrib import admin
from mysite import models

# Register your models here.

class MakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')\

class PModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'maker')\

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'pmodel', 'year', 'price')
    search_fields = ('nickname', 'pmodel__name', 'description', 'year', 'price')
    ordering = ('-year', 'price')

class PPhotoAdmin(admin.ModelAdmin):
    list_display = ( 'product','description')

admin.site.register(models.Maker, MakerAdmin)
admin.site.register(models.PModel, PModelAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.PPhoto, PPhotoAdmin)