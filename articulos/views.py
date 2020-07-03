from django.shortcuts import render, HttpResponse

# Create your views here.

def articulos(request):
    return render(request, "articulos/index.html")