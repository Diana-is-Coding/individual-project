from django.contrib import admin
from .models import Food, Medicine, NeededItem 

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ('category',)

# Register your models here.
admin.site.register(Food)
admin.site.register(Medicine)
admin.site.register(NeededItem)