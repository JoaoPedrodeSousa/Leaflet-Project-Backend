# Generated by Django 5.1.7 on 2025-03-27 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageRepository', '0003_remove_image_imagepath_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
