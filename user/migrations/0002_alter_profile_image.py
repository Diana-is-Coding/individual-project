# Generated by Django 5.0.6 on 2024-08-05 21:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='media/default.jpg', max_length=255, verbose_name='image'),
        ),
    ]