# Generated by Django 4.2.5 on 2023-09-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_remove_shopimport_yml_url_shopimport_yml_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopimport',
            name='yml_file',
        ),
        migrations.AddField(
            model_name='shopimport',
            name='yml_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]