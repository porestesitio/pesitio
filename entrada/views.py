from django.shortcuts import render

# Create your views here.

def entrada(request):
    return render(request, "entrada/index.html")