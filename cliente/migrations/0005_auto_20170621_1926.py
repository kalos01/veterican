# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-22 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20170621_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(default='Sin raza', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='direccion_domi',
            field=models.CharField(default='No tiene direcci\xf3n', max_length=225, null=True),
        ),
    ]
