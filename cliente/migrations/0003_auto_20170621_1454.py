# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-21 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20170621_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='direccion_domi',
            field=models.CharField(blank=True, max_length=225),
        ),
    ]