# Generated by Django 3.0.5 on 2020-10-05 10:16

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoCrudApp', '0005_auto_20201005_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('route_title', models.CharField(max_length=40)),
                ('route_author', models.CharField(max_length=30)),
                ('route_rank', models.IntegerField()),
                ('route_type', models.BooleanField(default=True)),
                ('route_img', models.URLField(max_length=1000)),
                ('placemant_and_belay_anchor', models.IntegerField(default=1)),
                ('route_description', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Pages',
            new_name='Page',
        ),
        migrations.DeleteModel(
            name='Routes',
        ),
        migrations.RenameModel(
            old_name='Regions',
            new_name='Region',
        ),
        migrations.AddField(
            model_name='route',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoCrudApp.Region'),
        ),
    ]