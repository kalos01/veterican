#encoding:utf-8
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('cliente.urls', namespace = 'cliente')),
    url(r'^', include('userInf.urls', namespace = 'empleado')),
    url(r'^', include('consulta.urls', namespace = 'consulta')),
    url(r'^', include('boleta.urls', namespace = 'boleta')),
	url(r'^$', views.auth_login, name = 'iniciarSesion'),
	url(r'^salir/$', views.logOut, name = 'CerrarSesion'),
	url(r'^home/$', views.bienvenido, name = 'home'),
]
