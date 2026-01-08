from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    """Formulario para crear y editar personas."""
    
    class Meta:
        model = Persona
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 
                  'direccion', 'ciudad', 'aseguradora_salud']
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 12.345.678-9'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre'
            }),
            'apellido_paterno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese apellido paterno'
            }),
            'apellido_materno': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese apellido materno'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese dirección'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese ciudad'
            }),
            'aseguradora_salud': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
