from django.contrib import admin
from .models import Goods

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ('category',)

# Register your models here.
admin.site.register(Goods, GoodsAdmin)