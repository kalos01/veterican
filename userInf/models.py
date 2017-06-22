#encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_unicode

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class TipoEmpleado(models.Model):
	tipo = models.CharField(max_length=225)

	def __str__(self):
		return  self.tipo

	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode(self.tipo)

	class Meta:
		ordering = ('id',)


@python_2_unicode_compatible
class Turno(models.Model):
	descripcion = models.CharField(max_length=225)

	def __str__(self):
		return  self.descripcion
		
	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode(self.descripcion)

	class Meta:
		ordering = ('id',)


def validate_length_DNI(value,length=8):
	if len(str(value))!=length:
		raise ValidationError(u'(%s) el DNI debe ser de 8 digitos' % value)


def validate_length_cell(value,length=9):
	if len(str(value))!=length:
	   	raise ValidationError(u'(%s) el numero debe ser de 9 digitos' % value)


def validate_type_Value(value):
	try:
		if type(int(value))!=int:
		   	raise ValidationError(u'(%s), debe ser numerico' % value)
	except Exception as e:
	   	raise ValidationError(u'(%s), debe ser numerico' % value)
	   	

@python_2_unicode_compatible
class Userinf(User):
	DNI = models.CharField(max_length=8, blank=False, null=False, unique = True, 
							error_messages={'blank': 'Campo vacio!', 'null': 'Campo vacio!','invalid': 'Dato invalido','unique':'Numero ya registrado'},
							validators=[validate_length_DNI, validate_type_Value])
	direccion_domi = models.CharField(max_length=225)
	fech_nacimiento = models.DateField(blank=False, null=False)
	cell = models.CharField(max_length=9, blank=False, null=False, unique = True, 
							error_messages={'blank': 'Campo vacio!', 'null': 'Campo vacio!','invalid': 'Dato invalido','unique':'Numero ya registrado'},
							validators=[validate_length_cell, validate_type_Value])
	tipoEmpleado = models.ForeignKey(TipoEmpleado)  # codigo
	turno = models.ForeignKey(Turno)  # codigo

	def __str__(self):
		return  ('%s - %s %s ( %s - %s )' % (self.username, self.first_name, self.last_name, self.tipoEmpleado, self.turno)).title()
		
	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode(('%s - %s %s ( %s - %s )' % (self.username, self.first_name, self.last_name, self.tipoEmpleado, self.turno)).title())

	class Meta:
		ordering = ('id',)
		verbose_name = 'Usuario Empleado'
		verbose_name_plural ='Usuarios Empleados'

	


