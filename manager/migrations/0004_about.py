# Generated by Django 5.1.7 on 2025-03-19 14:52

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imaage')),
            ],
        ),
    ]
