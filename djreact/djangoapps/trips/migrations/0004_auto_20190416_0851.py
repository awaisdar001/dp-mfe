# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-16 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_trip_gear'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['name'], 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'ordering': ['name'], 'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'ordering': ['name', 'verified']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tripitinerary',
            options={'ordering': ['trip', 'day'], 'verbose_name_plural': 'Trip Itineraries'},
        ),
        migrations.RemoveField(
            model_name='trip',
            name='cancelation_policy',
        ),
        migrations.RemoveField(
            model_name='tripitinerary',
            name='title',
        ),
        migrations.AddField(
            model_name='host',
            name='cancelation_policy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='_cancelation_policy',
            field=models.TextField(blank=True, null=True, verbose_name=b'Cancelation Policy Override'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='facility',
            name='slug',
            field=models.SlugField(blank=True, max_length=85, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='host',
            name='slug',
            field=models.SlugField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tripitinerary',
            name='description',
            field=models.TextField(default=b''),
        ),
    ]