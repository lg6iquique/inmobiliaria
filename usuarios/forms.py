from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno', 'telefono', 'direccion', 'ciudad')

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if Usuario.objects.filter(rut=rut).exists():
            raise forms.ValidationError("Ya existe un usuario con este RUT.")
        return rut

class UsuarioChangeForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('rut', 'nombres', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'direccion', 'ciudad', 'is_active')

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        # Exclude current instance from check
        if Usuario.objects.filter(rut=rut).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un usuario con este RUT.")
        return rut
