#encoding:utf-8
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm

# Create your views here.
def add_user(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/home/?next=%s' % request.path)
	if request.method == "POST":
		form = UserForm(request.POST or None)
		if form.is_valid:
			try:
				formulario = form.save(commit = False)
				# antes de guardar cambiamos el algoritmo  para el password
				formulario.set_password(form.cleaned_data['password'])
				# guardamos datos
				formulario.save()
				return HttpResponseRedirect('/home/')
			except AttributeError:
				print("Los campos no son compatibles")
			except ValueError:
 				Mensaje = "Nombre o email ya existen estan registrados"
				return render(request, 'empleado/empleado_form.html', locals())
	else:
		form =  UserForm()
	return render(request, 'empleado/empleado_form.html', locals())
