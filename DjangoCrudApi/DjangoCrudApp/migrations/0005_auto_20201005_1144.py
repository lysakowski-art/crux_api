# Generated by Django 3.0.5 on 2020-10-05 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoCrudApp', '0004_regions'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='language',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='page_content',
            field=models.TextField(),
        ),
    ]
