# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-21 19:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boleta', '0005_auto_20170621_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='dateBoleta',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 21, 14, 54, 15, 61000), editable=False),
        ),
    ]
