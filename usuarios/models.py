from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que extiende AbstractUser.
    Se añaden campos específicos como RUT, apellidos separados y otros datos de contacto.
    """
    rut = models.CharField(max_length=12, unique=True, verbose_name='RUT')
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name='Teléfono')
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name='Dirección')
    ciudad = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ciudad')
    
    # Campos de auditoría
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    # El campo 'activo' se gestiona con is_active de AbstractUser, pero si se requiere explícito:
    # is_active ya existe en AbstractUser y es el estándar para borrado lógico.

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.rut} - {self.username}"

    def get_nombre_completo(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
