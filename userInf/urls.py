#encoding:utf-8
from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Propietario
	url(r'^crearEmpleado/$',views.add_user,name = 'crearEmpleado'),
	]