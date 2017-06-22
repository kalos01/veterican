#encoding:utf-8
from __future__ import unicode_literals

from django.shortcuts import render,  redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import F, Q
from django.template import loader

from .models import Mascota, Propietario
# Create your views here.

class PropietarioList(ListView):
	model = Propietario


class PropietarioDetail(DetailView):
	model = Propietario


class PropietarioCreation(CreateView):
    model = Propietario
    success_url = reverse_lazy('cliente:listado')
    fields = ['nombre','ape_pat','ape_mat','DNI','direccion_domi','cell']


class PropietarioUpdate(UpdateView):
    model = Propietario
    success_url = reverse_lazy('cliente:listado')
    fields = ['nombre','ape_pat','ape_mat','DNI','direccion_domi','cell']


class PropietarioDelete(DeleteView):
    model = Propietario
    success_url = reverse_lazy('cliente:listado')


def PropietarioBuscar(request):
    query = request.POST.get("q")
    query_list = Propietario.objects.all()
    if query:
        query_list = query_list.filter(Q(nombre__icontains=query)|Q(ape_pat__icontains=query)|Q(ape_mat__icontains=query)
                                        |Q(DNI__icontains=query)|Q(direccion_domi__icontains=query)|Q(cell__icontains=query))
    context = {
        'object_list': query_list,
        }
    return render(request,"cliente/propietario_list.html", context )


def ListarMascota(request, pk):
    try:
        propietario = Propietario.objects.get(pk = pk)
        mascotas = Mascota.objects.all().filter(Propietario__id = pk)
        template = loader.get_template('cliente/mascota_list.html')
        detal = {
            'propietario': propietario,
            'object_list': mascotas,
            }
    except Propietario.DoesNotExist:
        return redirect('/home/')
    return HttpResponse(template.render(detal, request))

def MascotaList(request):
    mascotas = Mascota.objects.all().filter(estado_interno = True)
    template = loader.get_template('cliente/mascota_list.html')
    detal = {
        'object_list': mascotas,
        }
    return HttpResponse(template.render(detal, request))


class MascotaCreation(CreateView):
    model = Mascota
    success_url = reverse_lazy('cliente:listado')
    fields = ['raza','nombre','fech_nacimiento','Propietario','especie','estado_interno']


class MascotaDetail(DetailView):
    model = Mascota


class MascotaUpdate(UpdateView):
    model = Mascota
    success_url = reverse_lazy('cliente:listado')
    fields = ['raza','nombre','fech_nacimiento','especie','estado_interno']

class MascotasUpdate(UpdateView):
    model = Mascota
    success_url = reverse_lazy('cliente:listadoMascotas')
    fields = ['estado_interno']


class MascotaDelete(DeleteView):
    model = Mascota
    success_url = reverse_lazy('cliente:listado')
