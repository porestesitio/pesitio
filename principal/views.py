from django.shortcuts import render, HttpResponse

# Create your views here.

def principal(request):
    return render(request, "principal/index.html")