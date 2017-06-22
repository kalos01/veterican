#encoding:utf-8
from __future__ import unicode_literals

from django.contrib import admin

from .models import Propietario, Mascota
from .forms  import PropietarioForm
# Register your models here.

class AdminPropietario(admin.ModelAdmin):
    class Meta:
        model=Propietario


class AdminMascota(admin.ModelAdmin):
    class Meta:
        model=Mascota


admin.site.register(Propietario)
admin.site.register(Mascota)