from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

from ..models import Egresos

# "ubicacion" y "desc" son propiedades que se muestran como info adicional en la página
UBICACION = "Egresos"
INDEX = "/egresos"
# EGRESOS


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def egresos(request):
    registro = Egresos.objects.all()
    context = {
        "registro": registro,
        "ubicacion": UBICACION,
        "desc": "Registro de gastos de la empresa"
    }
    return render(request, 'egresos/index_egreso.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def agregar_egresos(request):
    context = {
        "ubicacion": UBICACION,
        "desc": "Registro de gastos de la empresa"
    }
    return render(request, 'egresos/agregar_egreso.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def validar_egresos(request):
    categoria = request.POST['txtCategoria']
    descripcion = request.POST['txtDescripcion']
    costos = request.POST['txtCostos']

    Egresos.objects.create(
        categoria=categoria,
        descripcion=descripcion,
        costos=costos
    )
    messages.add_message(request,
                         messages.SUCCESS,
                         f'Se guardó nuevo registro {categoria} por {costos} soles'
                         )
    return redirect(INDEX)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def editar_egreso(request, id):
    item = Egresos.objects.get(id=id)
    context = {
        "ubicacion": UBICACION,
        "egreso": item
    }
    return render(request, 'egresos/editar_egreso.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def validar_edicion_egresos(request, id):
    categoria = request.POST['txtCategoria']
    descripcion = request.POST['txtDescripcion']
    costos = request.POST['txtCostos']

    egreso = Egresos.objects.get(id=id)

    egreso.categoria = categoria
    egreso.descripcion = descripcion
    egreso.costos = costos

    egreso.save()
    messages.add_message(request,
                         messages.SUCCESS,
                         f'Se actualizó registro {categoria} - {descripcion}'
                         )
    return redirect(INDEX)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def eliminar_egresos(request, id):
    egreso = Egresos.objects.get(id=id)
    egreso.delete()
    messages.add_message(request,
                         messages.INFO,
                         f'Se eliminó el registro {egreso.categoria}'
                         )
    return redirect(INDEX)
