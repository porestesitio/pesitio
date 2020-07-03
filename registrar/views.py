from django.shortcuts import render, HttpResponse

# Create your views here.

def registrar(request):
    return render(request, "registrar/index.html")