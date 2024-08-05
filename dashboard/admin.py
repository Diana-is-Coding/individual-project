from django.contrib import admin
from .models import Goods, List

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    list_filter = ('category',)

class ListAdmin(admin.ModelAdmin):
    list_display = ('item', 'owner', 'added',)
    list_filter = ('owner',)


# Register your models here.
admin.site.register(Goods, GoodsAdmin)
admin.site.register(List, ListAdmin)
