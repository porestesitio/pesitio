from django.shortcuts import render, HttpResponse

# Create your views here.

def articulos(request):
    return HttpResponse("Articulos")