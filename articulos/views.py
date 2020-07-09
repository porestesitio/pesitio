from django.shortcuts import render, HttpResponse
# from .models import Articulos, Familia, Medida
# from .forms import ArticuloForm

# Create your views here.

def varticulos(request):
    return render(request, "articulos/index.html")

# def vnuevo(request):
#     data = {
#         'form': ArticuloForm()
#     }
# 
#     if request.method == 'POST':
#         formulario = ArticuloForm(request.POST, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             data['mensaje'] = 'Guardado correctamente'
#         data['form'] = formulario
#     
#     return render(request, 'articulo/nuevo.html')

#def vedita(request, id):
#    articulo = Articulos.objects.get(id=id)
#    data = {
#        'form': ArticuloForm(instance=articulo)
#    }

#    if request.method == 'POST':
#        formulario = ArticuloForm(request.POST, instance=articulo, files=request.FILES)
#        if formulario.is_valid():
#            formulario.save()
#            data['mensaje'] = 'Modificado correctamente'
 #       data['form'] = ArticuloForm(instance=articulos.objects.get(id=id))
    
 #   return render(request, 'articulo/edita.html')