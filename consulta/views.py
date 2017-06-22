#encoding:utf-8
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader  
from .forms import ConsultaForm

# Create your views here.
def CreateConsulta(request):
	if request.method =='POST':
		form = ConsultaForm(request.POST, request.FILES)
		if form.is_valid():
			producto = form.save(commit=False)
			producto.save()
			return HttpResponseRedirect('/boleta/new')
	else:
		form = ConsultaForm()
		template = loader.get_template('consulta/consulta_form.html')
		context = {
		'form': form,
		'mensaje': 'Error al ingresar',
		}
	return HttpResponse(template.render(context, request))