#encoding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from .models import TipoEmpleado, Turno, Userinf
from .forms import UserForm
from django.contrib.auth.forms import UserChangeForm

# Register your models here. 

@admin.register(Turno)
class AdminTurno(admin.ModelAdmin):
    class Meta:
        model=Turno


@admin.register(TipoEmpleado)
class AdminTipoEmpleado(admin.ModelAdmin):
    class Meta:
        model=TipoEmpleado


@admin.register(Userinf)
class AdminUserinf(admin.ModelAdmin):
    list_display = ["username","first_name","last_name","DNI","direccion_domi","cell","turno","tipoEmpleado"]
    form = UserForm
    list_filter = ["turno","tipoEmpleado"]
    list_editable = ["turno","tipoEmpleado"]
    search_fields = ["username","first_name","last_name","DNI","direccion_domi","cell","turno","tipoEmpleado"]
    list_display_links =["username"]
    class Meta:
    	model=Userinf



