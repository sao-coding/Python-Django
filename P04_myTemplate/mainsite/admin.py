from django.contrib import admin
from .models import Tv_list, Engtv_list, Car_list
# Register your models here.

class tvAdmin(admin.ModelAdmin):
    list_display = ('tvname', 'tvcode')

class engtvAdmin(admin.ModelAdmin):
    list_display = ('tvname', 'tvcode')

class carAdmin(admin.ModelAdmin):
    list_display = ('car_maker', 'car_model', 'car_price', 'car_qty')

admin.site.register(Tv_list, tvAdmin)
admin.site.register(Engtv_list, engtvAdmin)
admin.site.register(Car_list, carAdmin)