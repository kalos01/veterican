# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-21 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='especie',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]
