from django.shortcuts import render, HttpResponse

# Create your views here.

def empleos(request):
    return HttpResponse("Empleos")