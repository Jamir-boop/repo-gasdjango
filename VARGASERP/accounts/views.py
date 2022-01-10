from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group, User

from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# Create your views here.

INDEX = '/'

def login_user(request):
    if request.user.is_authenticated:
        return redirect(INDEX)
    else:
        if request.method == 'POST':
            user = request.POST['user']
            password = request.POST['password']
            user = authenticate(request, username=user, password=password)
            if user is not None:
                login(request, user)
                return redirect(INDEX)
            else:
                messages.success(request, ("Error al iniciar sesion intente nuevamente"))
                return redirect('login')
        else:
            return render(request, 'authentication/login.html', {})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def register_user(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data['username']
        group = form.cleaned_data['group']
        if request.user.groups.filter(name='admin'):
            add_group = Group.objects.get(name=group)
        else:
            add_group = Group.objects.get(name='vendedor')
        user.groups.add(add_group)

        messages.success(request, f'El {add_group} {username} fue creado correctamente. 🙂')
        return redirect('login')

    else:
        form = CreateUserForm()

    context = {'form': form }
    return render(request, 'authentication/register.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, ("Se a cerrado sesion"))
    return redirect('login')