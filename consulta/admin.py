#encoding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from .models import Consulta

# Register your models here.

class AdminConsulta(admin.ModelAdmin):
    list_display = ["__str__"]
    class Media:
    	js = ['tiny_mce/tiny_mce.js', 'js/textareas.js']
    class Meta:
        model=Consulta
        

admin.site.register(Consulta)