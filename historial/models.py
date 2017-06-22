#encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from userInf.models import Userinf
from cliente.models import Mascota

from django.utils.encoding import smart_unicode

from django.utils.encoding import python_2_unicode_compatible

from tinymce.models import HTMLField

# Create your models here.

@python_2_unicode_compatible
class Historial(models.Model):
	dateHistorial = models.DateTimeField(default=datetime.now(), blank=True,editable=False)
	descripcion = models.TextField()
	empleado = models.ForeignKey(Userinf)
	mascota = models.ForeignKey(Mascota)

	def __str__(self):
		return  self.descripcion

	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode(self.descripcion)

	class Meta:
		ordering = ('id',)
		verbose_name = 'Historial'
		verbose_name_plural ='Historiales'
