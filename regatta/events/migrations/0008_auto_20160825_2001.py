# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='event',
            field=models.ForeignKey(default=1, help_text='event this race is part of', on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='number',
            field=models.PositiveIntegerField(default=1, help_text='number of race in an event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='wind_speed_max',
            field=models.PositiveIntegerField(help_text='maximum wind speed during the race in beaufort'),
        ),
        migrations.AlterField(
            model_name='race',
            name='wind_speed_min',
            field=models.PositiveIntegerField(help_text='minimum wind speed during the race in beaufort'),
        ),
    ]
