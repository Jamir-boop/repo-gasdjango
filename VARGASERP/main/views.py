from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TestAdmin, Egresos
from django.contrib.auth.decorators import login_required

from accounts.decorators import allowed_users

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def egresos(request):
    egresos = Egresos.objects.all()
    context = {"egresos" : egresos}
    return render(request, 'egresos/index.html', context) 

def agregar_egresos(request):
    return render(request, 'egresos/agregar_egreso.html') 

def validar_egresos(request):
    categoria = request.POST['txtCategoria']
    descripcion = request.POST['txtDescripcion']
    costos = request.POST['txtCostos']

    egreso = Egresos.objects.create(
        categoria = categoria, descripcion = descripcion, costos = costos
    )

    return redirect('/egresos')
    
def editar_egreso(request, id):
    egreso = Egresos.objects.get(id=id)
    return render(request, 'egresos/editar_egreso.html', {"egreso": egreso}) 

def validar_edicion_egresos(request, id):
    categoria = request.POST['txtCategoria']
    descripcion = request.POST['txtDescripcion']
    costos = request.POST['txtCostos']
    
    egreso = Egresos.objects.get(id=id)

    egreso.categoria = categoria
    egreso.descripcion = descripcion
    egreso.costos = costos

    egreso.save()
    return redirect('/egresos')

def eliminar_egresos(request, id):
    egreso = Egresos.objects.get(id=id)
    egreso.delete()
    return redirect('/egresos')
