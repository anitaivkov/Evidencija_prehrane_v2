from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import *

## Create your views here.

def homepage(request):
    return HttpResponse('Naslovnica evidencije prehrane')

class NamirnicaLista(ListView):
    model = Namirnica

