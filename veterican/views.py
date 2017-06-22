#encoding:utf-8
from __future__ import unicode_literals

from django.shortcuts import render,  redirect

from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# logear usuario
def auth_login(request):
	# if not request.user.is_anonymous():  request.path request.user.username
	if request.user.is_authenticated():
		return redirect('home/?next=%s' % request.path)
	if request.method == 'POST':
		action = request.POST.get('action', None)
		username = request.POST.get('username',None)
		password = request.POST.get('password', None)
		if action == 'login':
			try:
				user = authenticate(username=username, password=password)
				if user is not None and user.is_active:
					login(request, user)
			except UserWarning as e:
				return render(request, 'logueo/login.html', {'mensaje' : 'Usuario invalido.'})
			except AttributeError as e:
				return render(request, 'logueo/login.html', {'mensaje' : 'Usuario invalido.'})
			except Exception as e:
				return render(request, 'logueo/login.html', {'mensaje' : 'Usuario invalido.'})
			return redirect('/home/')
	context ={}
	return render(request, 'logueo/login.html', locals())


# desloguear
def logOut(request):
    auth_logout(request)
    return redirect('/')


# para que te redirija a una pagina que necesite loguearse
# ejemplo:
@login_required(login_url='/')
def bienvenido(request):
    return render(request, 'veterinaria/home.html', locals())

