from django import forms
from .models import Propiedad, PropiedadImagen

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class PropiedadForm(forms.ModelForm):
    imagenes = MultipleFileField(
        label='Cargar Imágenes', 
        required=False, 
        help_text='Seleccione múltiples imágenes con Ctrl/Cmd + Clic'
    )

    class Meta:
        model = Propiedad
        fields = [
            'codigo', 'estado', 'destacada',
            'tipo_propiedad', 'operacion',
            'superficie_total_m2', 'superficie_construida_m2', 'numero_piezas', 'numero_banos', 'estacionamientos', 'bodegas',
            'precio_venta_clp', 'precio_venta_uf', 'precio_arriendo_clp', 'precio_arriendo_uf',
            'region', 'comuna', 'direccion', 'latitud', 'longitud'
        ]
        widgets = {
            'latitud': forms.NumberInput(attrs={'step': 'any'}),
            'longitud': forms.NumberInput(attrs={'step': 'any'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        total = cleaned_data.get('superficie_total_m2')
        construida = cleaned_data.get('superficie_construida_m2')

        if total and construida and construida > total:
            self.add_error('superficie_construida_m2', 'La superficie construida no puede ser mayor a la total.')
        
        return cleaned_data
