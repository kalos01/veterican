#encoding:utf-8
from django  import forms

from .models import Consulta
from tinymce.widgets import TinyMCE

class ConsultaForm(forms.ModelForm):
	descripcionConsulta = forms.CharField(widget=TinyMCE(attrs={'cols': 400, 'rows': 500}))
	class Meta:
		model = Consulta
		fields = '__all__'


