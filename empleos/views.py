from django.shortcuts import render, HttpResponse

# Create your views here.

def empleos(request):
    return render(request, "empleos/index.html")