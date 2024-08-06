from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200,)
    phone = models.CharField(max_length=20,)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f'{self.customer.username}-Profile'