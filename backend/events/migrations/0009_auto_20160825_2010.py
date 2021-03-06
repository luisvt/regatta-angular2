# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20160825_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='weather',
        ),
        migrations.AddField(
            model_name='race',
            name='sky_condition',
            field=models.IntegerField(choices=[(1, 'cloudy'), (2, 'mostly cloudy'), (3, 'partly sunny'), (4, 'mostly sunny'), (5, 'sunny')], default=1, help_text='weather during the race'),
            preserve_default=False,
        ),
    ]
