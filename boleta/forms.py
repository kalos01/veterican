#encoding:utf-8
from django  import forms

from .models import Boleta

class BoletaForm(forms.ModelForm):
	class Meta:
		model = Boleta
		fields = '__all__'


