from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
CATEGORY = (
    ('Pantry', 'Pantry'),
    ('Chilled', 'Chilled'),
    ('Frozen', 'Frozen'),
    ('Supliment', 'Supliment'),
    ('Prescription', 'Prescription'),
)

TYPE = (
    ('grams', 'grams'),
    ('ml', 'ml'),
    ('bags', 'bags'),
    ('cans', 'cans'),
    ('packs', 'packs'),
    ('kg', 'kg'),
    ('doses', 'doses'),
)

class Goods(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField( null=True)
    units = models.CharField(choices=TYPE, null=True)
    added = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Inventory Items'
   
    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.units}'
        
class List(models.Model): 
    item = models.ForeignKey(Goods, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item} for {self.owner} added to list on {self.added}'