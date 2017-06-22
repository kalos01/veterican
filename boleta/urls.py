#encoding:utf-8
from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^Boleta/new/$',views.PropietarioList, name='listProBoleta'),
	url(r'^Boleta/reg/(?P<pk>\d+)/$',views.BoletaXClienteCreate, name='CrearBoleta'),
	]
