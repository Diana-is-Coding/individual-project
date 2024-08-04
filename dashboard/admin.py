from django.contrib import admin
from .models import Food, Medicine, Grocery 

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ('category',)

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'doses',)
    list_filter = ('category',)

# Register your models here.
admin.site.register(Food, FoodAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Grocery)