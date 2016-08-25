# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_person_sailing_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(help_text='start of the race')),
                ('end_time', models.DateTimeField(help_text='end of the race')),
                ('weather', models.IntegerField(choices=[(1, 'sunny'), (2, 'cloudy'), (3, 'partly cloudy')], help_text='weather during the race')),
                ('wind_speed_min', models.PositiveIntegerField(help_text='minimum wind speed during the race')),
                ('wind_speed_max', models.PositiveIntegerField(help_text='maximum wind speed during the race')),
            ],
        ),
    ]
