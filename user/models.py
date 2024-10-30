from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.templatetags.static import static
from django_resized import ResizedImageField

# Create your models here.
class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200,)
    phone = models.CharField(max_length=20,)
    image = ResizedImageField(size=[400,400], quality=85, upload_to='static/cloudinary/images', null=True, blank=True)

    def __str__(self):
        return f'{self.customer.username}-Profile'