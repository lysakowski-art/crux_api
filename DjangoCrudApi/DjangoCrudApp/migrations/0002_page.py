# Generated by Django 3.0.5 on 2020-09-23 15:17

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoCrudApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('page_title', models.CharField(max_length=50)),
                ('page_content', models.TextField(max_length=600)),
            ],
        ),
    ]
