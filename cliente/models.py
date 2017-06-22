#encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_unicode
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

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


def validar_str(value,length=9):
    if not value.isalpha():
        raise ValidationError(u'(%s), debe ser una palabra' % value)


def validate_letra_M(value):
    if not value.istitle():
        raise ValidationError(u'(%s), primera letra mayuscula' % value)


@python_2_unicode_compatible
class Propietario(models.Model):
	nombre = models.CharField(max_length=225, validators=[validar_str, validate_letra_M],
							  error_messages={'blank': 'Campo vacio!', 'null': 'Campo vacio!','invalid': 'Dato invalido'})
	ape_pat = models.CharField(max_length=225, validators=[validar_str, validate_letra_M],
							  error_messages={'blank': 'Campo vacio!', 'null': 'Campo vacio!','invalid': 'Dato invalido'})
	ape_mat = models.CharField(max_length=225, validators=[validar_str, validate_letra_M],
							  error_messages={'blank': 'Campo vacio!', 'null': 'Campo vacio!','invalid': 'Dato invalido'})
	DNI = models.CharField(max_length=8 , validators=[validate_length_DNI, validate_type_Value],unique = True)
	direccion_domi = models.CharField(max_length=225, null=True, blank=False, default="No tiene dirección")
	cell = models.CharField(max_length=9, validators=[validate_length_cell, validate_type_Value],unique = True)
	
	def __str__(self):
		return  '%s - %s %s' % (self.nombre, self.ape_pat, self.ape_mat)

	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode('%s - %s %s' % (self.nombre, self.ape_pat, self.ape_mat))

	class Meta:
		ordering = ('id',)


@python_2_unicode_compatible
class Mascota(models.Model):
	Propietario = models.ForeignKey(Propietario)  # codigo
	especie = models.CharField(max_length=225)
	raza = models.CharField(max_length=225, null=True , blank=False,  default="Sin raza")
	nombre = models.CharField(max_length=225)
	fech_nacimiento = models.DateField( blank=True )
	estado_interno = models.BooleanField(null=False,default=False)
	
	def __str__(self):
		return  "%s - %s %s" % (self.Propietario, self.especie, self.nombre)

	def __unicode__(self):		# __unicode__ on Python 2
		return smart_unicode("%s - %s %s" % (self.Propietario, self.especie, self.nombre))

	class Meta:
		ordering = ('id',)
