from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("egresos/", views.egresos, name="egresos"),
    path("agregar-egreso/", views.agregar_egresos, name="agregar_egresos"),
    path("validar-egreso/", views.validar_egresos, name="validar_egresos"),
    path("editar-egreso/<id>", views.editar_egreso, name="editar_egreso"),
    path("validar-edicion-egreso/<id>", views.validar_edicion_egresos, name="validar_edicion_egresos"),
    path("eliminar-egreso/<id>", views.eliminar_egresos, name="eliminar_egresos"),
]