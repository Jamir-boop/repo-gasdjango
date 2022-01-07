from django.shortcuts import render
from django.http import HttpResponse
from .models import TestAdmin

# Create your views here.
def index(request):
    context = {}

    return render(request, 'main/index.html', context)

def test(request):
    admins = TestAdmin.objects.all()
    context = {'admins': admins}

    return render(request, 'main/test.html', context)
