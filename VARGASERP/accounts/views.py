from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group, User

from .forms import CreateUserForm

# Create your views here.

def register_user(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data['username']

        group = Group.objects.get(name="admin_local")
        user.groups.add(group)

        messages.success(request, f'El administrador {username} fue creado correctamente.')
        return redirect('main:index')

    else:
        form = CreateUserForm()

    context = {'form': form }

    return render(request, 'authentication/register.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST['user']
            password = request.POST['password']
            user = authenticate(request, username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                messages.success(request, ("Error al iniciar sesion intente nuevamente"))
                return redirect('login')
        else:
            return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Se a cerrado sesion"))
    return redirect('main:index')