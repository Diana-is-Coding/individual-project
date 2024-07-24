from django.db import models

# Create your models here.
CATEGORY = (
    ('Pantry', 'Pantry'),
    ('Chilled', 'Chilled'),
    ('Frozen', 'Frozen'),
)

class Kitchen(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)