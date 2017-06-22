#encoding:utf-8
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from cliente.models import Propietario
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import BoletaForm
from .models import Boleta

# Create your views here.

def PropietarioList(request):
	propietarios = Propietario.objects.all()
	template = loader.get_template('boleta/boleta_list.html')
	detal = {
		'object_list': propietarios,
	}
	return HttpResponse(template.render(detal, request))


def BoletaXClienteCreate(request, pk):
	propietario = get_object_or_404(Propietario,pk = pk)
	if request.method =='POST':
		form = BoletaForm(request.POST, request.FILES)
		if form.is_valid():
			boleta = form.save(commit=False)
			# if not boleta.propietario:
			boleta.propietario = propietario
			boleta.save()
			detalleBoleta = Boleta.objects.get(id=boleta.id)
			detal = {
				'boleta': detalleBoleta,
			}
			template = loader.get_template('boleta/boleta_detail.html')
			return HttpResponse(template.render(detal, request))
	template = loader.get_template('boleta/boleta_form.html')
	form = BoletaForm()
	detal = {
	'propietario': propietario, 
	'form': form, 
	}
	return HttpResponse(template.render(detal, request))
