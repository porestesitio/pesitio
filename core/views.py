from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Se conecta ahora como: {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalido usuario o contaseña.")
        else:
            messages.error(request, "Invalido usuario o contraseña.")
    form = CustomUserForm()
    return render(request = request,
                    template_name = "registration/registrar.html",
                    context={"form":form})

#   data = {
#        'form':CustomUserForm()
#    }
#    
#    if request.method == 'POST':
#        formulario = CustomUserForm(request.POST)
#        if formulario.is_valid():
#            formulario.save()
#            # redireccion
#            username = formulario.cleaned_data['username']
#            password = formulario.cleaned_data['password1']
#            user = authenticate(username=username, password=password)
#            login(request,user)
            # return redirect(to='')
#            return redirect('principal/index.html',data)
#    return render(request, 'registration/registrar.html', data)