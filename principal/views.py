from django.shortcuts import render, HttpResponse

# Create your views here.

def articulos(request):
    return HttpResponse("Articulos")

def blog(request):
    return HttpResponse("Blog")

def contacto(request):
    return HttpResponse("Contacto")

def empleos(request):
    return HttpResponse("Empleos")

def login(request):
    return HttpResponse("Login")

def inicio(request):
    return HttpResponse("Inicio")

#def registro(request):
#    return HttpResponse("Registro")

def servicios(request):
    return HttpResponse("Servicios")