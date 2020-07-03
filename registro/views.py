from django.shortcuts import render, HttpResponse
from registro.forms import FrmRegistro

# Create your views here.

def registro(request):
    return HttpResponse("Registro")
