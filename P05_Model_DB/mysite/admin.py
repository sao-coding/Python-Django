from django.contrib import admin
from .models import Maker, PModel, Product, PPhoto

# Register your models here.

class MakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')\

class PModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'maker')\

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'pmodel', 'year', 'price')

class PPhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'product')

admin.site.register(Maker, MakerAdmin)
admin.site.register(PModel, PModelAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PPhoto, PPhotoAdmin)