from django.db import models

# Create your models here.
CATEGORY = (
    ('Pantry', 'Pantry'),
    ('Chilled', 'Chilled'),
    ('Frozen', 'Frozen'),
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
    
    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.units}'

class Medicine(models.Model):
    name = models.CharField(max_length=100, null=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class NeededItem(models.Model):
    item = models.CharField(null=True)
    category = models.CharField(choices=CATEGORY, null=True)
    checked = models.BooleanField(default=None)

    def __str__(self):
        return f'{self.item}'