from django.urls import path
from . import views
from .controller import controller_egresos

urlpatterns = [
    path("", views.index, name="index"),

    path("egresos/", controller_egresos.egresos, name="egresos"),
    path("agregar-egreso/", controller_egresos.agregar_egresos,
         name="agregar_egresos"),
    path("validar-egreso/", controller_egresos.validar_egresos,
         name="validar_egresos"),
    path("editar-egreso/<id>", controller_egresos.editar_egreso, name="editar_egreso"),
    path("validar-edicion-egreso/<id>", controller_egresos.validar_edicion_egresos,
         name="validar_edicion_egresos"),
    path("eliminar-egreso/<id>", controller_egresos.eliminar_egresos,
         name="eliminar_egresos"),
]
