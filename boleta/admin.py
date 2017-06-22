#encoding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from .models import TipoBoleta, Boleta

# Register your models here.

class AdminTipoBoleta(admin.ModelAdmin):
    class Meta:
        model=TipoBoleta



class AdminBoleta(admin.ModelAdmin):
    class Meta:
        model=Boleta


admin.site.register(Boleta)
admin.site.register(TipoBoleta)