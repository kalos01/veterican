# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-21 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleta', '0002_auto_20170621_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='dateBoleta',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 21, 3, 31, 4, 166000), editable=False),
        ),
    ]
