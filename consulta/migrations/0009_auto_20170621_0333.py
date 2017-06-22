# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-21 08:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0008_auto_20170621_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='dateConsulta',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 21, 3, 32, 53, 946000), editable=False),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='descripcionConsulta',
            field=tinymce.models.HTMLField(),
        ),
    ]
