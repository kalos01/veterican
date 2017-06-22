# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Historial

# Register your models here.

class AdminHistorial(admin.ModelAdmin):
    class Meta:
        model=Historial


admin.site.register(Historial)