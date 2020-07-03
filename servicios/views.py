from django.shortcuts import render, HttpResponse

# Create your views here.

def servicios(request):
    return render(request, "servicios/index.html")