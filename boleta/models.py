#encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from datetime import datetime  

from userInf.models import Userinf
from cliente.models import Propietario
from django.utils.encoding import smart_unicode
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class TipoBoleta(models.Model):
	tipo = models.CharField( max_length=50)
	monto = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return  '%s - %s $' %(self.tipo, self.monto)

	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode('%s - %s $' %(self.tipo, self.monto))

	class Meta:
		ordering = ('id',)



@python_2_unicode_compatible
class Boleta(models.Model):
	dateBoleta = models.DateTimeField(default=datetime.now(), blank=True,editable=False)
	propietario = models.ForeignKey(Propietario, null=True, blank=True)
	empleado = models.ForeignKey(Userinf)
	tipoBoleta = models.ForeignKey(TipoBoleta)

	def __str__(self):
		return '%s - %s (%s)' %(self.propietario, self.tipoBoleta, self.dateBoleta)

	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode('%s - %s (%s)' %(self.propietario, self.tipoBoleta, self.dateBoleta))

	class Meta:
		ordering = ('id',)