# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-21 06:37
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import userInf.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=225)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=225)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Userinf',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('DNI', models.CharField(error_messages={'blank': 'Campo vacio!', 'invalid': 'Dato invalido', 'null': 'Campo vacio!', 'unique': 'Numero ya registrado'}, max_length=8, unique=True, validators=[userInf.models.validate_length_DNI, userInf.models.validate_type_Value])),
                ('direccion_domi', models.CharField(max_length=225)),
                ('fech_nacimiento', models.DateField()),
                ('cell', models.CharField(error_messages={'blank': 'Campo vacio!', 'invalid': 'Dato invalido', 'null': 'Campo vacio!', 'unique': 'Numero ya registrado'}, max_length=9, unique=True, validators=[userInf.models.validate_length_cell, userInf.models.validate_type_Value])),
                ('tipoEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userInf.TipoEmpleado')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userInf.Turno')),
            ],
            options={
                'ordering': ('id',),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
