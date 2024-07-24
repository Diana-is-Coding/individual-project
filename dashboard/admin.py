from django.contrib import admin
from .models import Food, Medicine, NeededItem 


# Register your models here.
admin.site.register(Food)
admin.site.register(Medicine)
admin.site.register(NeededItem)