#encoding:utf-8
from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^Consulta/new$', views.CreateConsulta, name= 'CreateConsulta'),
]