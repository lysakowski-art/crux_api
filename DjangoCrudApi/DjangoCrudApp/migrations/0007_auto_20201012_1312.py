# Generated by Django 3.0.5 on 2020-10-12 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoCrudApp', '0006_auto_20201005_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='location',
        ),
        migrations.RemoveField(
            model_name='route',
            name='region',
        ),
        migrations.RemoveField(
            model_name='route',
            name='route_img',
        ),
    ]
