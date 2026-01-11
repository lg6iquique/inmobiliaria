from django.contrib import admin
from .models import Propiedad, PropiedadImagen

class PropiedadImagenInline(admin.TabularInline):
    model = PropiedadImagen
    extra = 1

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo_propiedad', 'comuna', 'operacion', 'estado', 'precio_venta_clp', 'precio_arriendo_clp')
    list_filter = ('estado', 'tipo_propiedad', 'operacion', 'comuna')
    search_fields = ('codigo', 'direccion', 'comuna')
    inlines = [PropiedadImagenInline]
