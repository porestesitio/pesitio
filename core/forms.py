from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from colorful.fields import RGBColorField
from colorful.forms import RGB_REGEX
from colorful.widgets import ColorFieldWidget

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

        labels={
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Correo',
            'username':'Usuario',
            'password1':'Contraseña',
            'password2':'Confirma',
        }

