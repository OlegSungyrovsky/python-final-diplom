# Generated by Django 4.2.5 on 2023-09-13 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_productinfo_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinfo',
            old_name='models',
            new_name='model',
        ),
    ]
