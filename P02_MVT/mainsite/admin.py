from django.contrib import admin
from .models import test, Product

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'qty', 'size')


admin.site.register(test)
admin.site.register(Product, productAdmin)