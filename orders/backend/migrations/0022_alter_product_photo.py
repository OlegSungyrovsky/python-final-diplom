# Generated by Django 4.2.5 on 2023-10-17 16:57

import backend.models
from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_alter_product_photo_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default='image/user_image/products_image/default_product_image.png', help_text='Max image size up to 800x800', null=True, upload_to=backend.models.get_path_image, verbose_name='Фото'),
        ),
    ]