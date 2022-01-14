from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.
# "ubicacion" y "desc" son propiedades que se muestran como info adicional en la página


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def index(request):
    context = {
        "ubicacion": "Inicio"
    }
    return render(request, 'index.html', context)
