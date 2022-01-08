from django.shortcuts import render
from django.http import HttpResponse
from .models import TestAdmin
from django.contrib.auth.decorators import login_required

from accounts.decorators import allowed_users

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'vendedor'])
def index(request):
    context = {}
    return render(request, 'main/index.html', context)