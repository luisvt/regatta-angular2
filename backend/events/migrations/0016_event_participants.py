# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_raceentryrelationship_calculated_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(through='events.Entry', to='events.Person'),
        ),
    ]
