# Generated by Django 5.1.7 on 2025-03-26 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageRepository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imagePath',
            field=models.CharField(default=''),
        ),
    ]
