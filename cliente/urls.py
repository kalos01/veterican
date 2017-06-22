#encoding:utf-8
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Propietario
	url(r'^Propietario/buscar$',views.PropietarioBuscar,name = 'buscar'),
	url(r'^Propietario/$',views.PropietarioList.as_view(), name='listado'),
	url(r'^Propietario/(?P<pk>[0-9]+)/$', views.PropietarioDetail.as_view(), name='PropietarioDetalle'),
	url(r'^Propietario/new$', views.PropietarioCreation.as_view(), name='PropietarioNuevo'),
	url(r'^Propietario/editar/(?P<pk>\d+)$', views.PropietarioUpdate.as_view(), name='edit'),
	url(r'^Propietario/borrar/(?P<pk>\d+)$', views.PropietarioDelete.as_view(), name='delete'),
	# Mascota
	url(r'^Propietario/mascota/(?P<pk>[0-9]+)/$',views.ListarMascota, name='ListarMascota'),
	url(r'^Propietario/mascota/detal/(?P<pk>[0-9]+)/$', views.MascotaDetail.as_view(), name='MascotaDetalle'),
	url(r'^Propietario/mascota/new$', views.MascotaCreation.as_view(), name='MascotaCreation'),
	url(r'^Propietario/mascota/editar/(?P<pk>\d+)$', views.MascotaUpdate.as_view(), name='mascotaEdit'),
	url(r'^Propietario/mascota/borrar/(?P<pk>\d+)$', views.MascotaDelete.as_view(), name='MascotaDel'),
	url(r'^Propietario/mascotas/$',views.MascotaList, name='listadoMascotas'),
	url(r'^Propietario/mascotas/editar/(?P<pk>\d+)$', views.MascotasUpdate.as_view(), name='mascotasEdit'),
    ]