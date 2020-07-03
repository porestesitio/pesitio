from django import forms

class FrmRegistro(forms.Form):

    nombre=forms.CharField()
    apellido=forms.CharField()
    correo=forms.EmailField()
    
