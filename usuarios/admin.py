from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    # Fieldsets controls the layout of the admin form on the "change" page.
    fieldsets = UserAdmin.fieldsets + (
        ('Información Personal Extra', {'fields': ('rut', 'apellido_paterno', 'apellido_materno')}),
        ('Contacto', {'fields': ('telefono', 'direccion', 'ciudad')}),
    )
    # Add sets controls the layout on the "add" page.
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Personal Extra', {'fields': ('rut', 'nombres', 'apellido_paterno', 'apellido_materno', 'email')}),
    )
    list_display = ('username', 'rut', 'email', 'nombres', 'apellido_paterno', 'is_active')
    search_fields = ('username', 'rut', 'email', 'nombres', 'apellido_paterno')

admin.site.register(Usuario, UsuarioAdmin)
