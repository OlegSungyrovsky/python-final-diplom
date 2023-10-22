# Generated by Django 4.2.5 on 2023-10-16 12:42

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_user_image_ppoi_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='image/products_image/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20),
        ),
    ]
