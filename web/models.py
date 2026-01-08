from django.db import models


class Persona(models.Model):
    """Modelo para almacenar información de personas."""
    
    ASEGURADORAS_CHOICES = [
        ('FONASA', 'FONASA'),
        ('ISAPRE_BANMEDICA', 'Isapre Banmédica'),
        ('ISAPRE_CONSALUD', 'Isapre Consalud'),
        ('ISAPRE_COLMENA', 'Isapre Colmena'),
        ('ISAPRE_CRUZ_BLANCA', 'Isapre Cruz Blanca'),
        ('ISAPRE_VIDA_TRES', 'Isapre Vida Tres'),
        ('OTRA', 'Otra'),
    ]
    
    rut = models.CharField(max_length=12, unique=True, verbose_name='RUT')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    aseguradora_salud = models.CharField(
        max_length=50,
        choices=ASEGURADORAS_CHOICES,
        verbose_name='Aseguradora de Salud'
    )
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['apellido_paterno', 'apellido_materno', 'nombre']
    
    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido_paterno}"
    
    def get_nombre_completo(self):
        """Retorna el nombre completo de la persona."""
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
