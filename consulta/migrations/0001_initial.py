# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-21 06:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateConsulta', models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 21, 1, 37, 40, 569000), editable=False)),
                ('descripcionConsulta', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]