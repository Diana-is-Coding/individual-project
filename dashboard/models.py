from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Pantry', 'Pantry'),
    ('Chilled', 'Chilled'),
    ('Frozen', 'Frozen'),
)

medCATEGORY = (
    ('Supliment', 'Supliment'),
    ('Prescription', 'Prescription'),
)

TYPE = (
    ('grams', 'grams'),
    ('ml', 'ml'),
    ('bags', 'bags'),
    ('cans', 'cans'),
    ('packs', 'packs'),
)

class Food(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField( null=True)
    units = models.CharField(choices=TYPE, null=True)
    
    class Meta:
        verbose_name_plural = 'Food'
   
    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.units}'

class Medicine(models.Model):
    name = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=20, choices=medCATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Med Cabinet'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Grocery(models.Model):
    item = models.ForeignKey(Food, on_delete=models.CASCADE)
    item = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    checked = models.BooleanField(default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Shopping List'

    def __str__(self):
        return f'{self.item}'