#encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime   
from userInf.models import Userinf
from cliente.models import Propietario
from django.utils.encoding import smart_unicode

from django.utils.encoding import python_2_unicode_compatible

from tinymce.models import HTMLField

# Create your models here.


@python_2_unicode_compatible
class Consulta(models.Model):
	dateConsulta = models.DateTimeField(default=datetime.now(), blank=True, editable = False)
	descripcionConsulta = HTMLField()
	propietario = models.ForeignKey(Propietario)
	empleado = models.ForeignKey(Userinf)

	def __str__(self):
		return  ' %s - %s ' % (self.descripcionConsulta, self.propietario )

	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode(' %s - %s ' % (self.descripcionConsulta, self.propietario ))

	class Meta:
		ordering = ('id',)