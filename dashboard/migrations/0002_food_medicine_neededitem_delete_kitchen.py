# Generated by Django 5.0.6 on 2024-08-02 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Pantry', 'Pantry'), ('Chilled', 'Chilled'), ('Frozen', 'Frozen')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('units', models.CharField(choices=[('grams', 'grams'), ('ml', 'ml'), ('bags', 'bags'), ('cans', 'cans'), ('packs', 'packs')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Supliment', 'Supliment'), ('Prescription', 'Prescription')], max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NeededItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField(default=None)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.medicine')),
            ],
        ),
        migrations.DeleteModel(
            name='Kitchen',
        ),
    ]
