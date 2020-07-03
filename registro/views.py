from django.shortcuts import render, HttpResponse
from registro.forms import FrmRegistro

# Create your views here.

def reg(request):
    return HttpResponse("Registro")
