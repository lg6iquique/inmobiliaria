from django.db import models
import os

class Propiedad(models.Model):
    ESTADOS = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
        ('VENDIDO', 'Vendido'),
        ('ARRENDADO', 'Arrendado'),
    ]
    TIPOS = [
        ('CASA', 'Casa'),
        ('DEPARTAMENTO', 'Departamento'),
        ('OFICINA', 'Oficina'),
        ('TERRENO', 'Terreno'),
        ('OTRO', 'Otro'),
    ]
    OPERACIONES = [
        ('VENTA', 'Venta'),
        ('ARRIENDO', 'Arriendo'),
        ('AMBOS', 'Venta y Arriendo'),
    ]

    # Identificación y estado
    codigo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Código')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVO', verbose_name='Estado')
    fecha_publicacion = models.DateField(auto_now_add=True, verbose_name='Fecha Publicación')
    destacada = models.BooleanField(default=False, verbose_name='Destacada')

    # Tipo y operación
    tipo_propiedad = models.CharField(max_length=20, choices=TIPOS, verbose_name='Tipo Propiedad')
    operacion = models.CharField(max_length=15, choices=OPERACIONES, verbose_name='Operación')

    # Superficie y distribución
    superficie_total_m2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Sup. Total m²')
    superficie_construida_m2 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Sup. Construida m²')
    numero_piezas = models.PositiveIntegerField(verbose_name='Nº Piezas')
    numero_banos = models.PositiveIntegerField(verbose_name='Nº Baños')
    estacionamientos = models.PositiveIntegerField(default=0, verbose_name='Estacionamientos')
    bodegas = models.PositiveIntegerField(default=0, verbose_name='Bodegas')

    # Valores
    precio_venta_clp = models.BigIntegerField(default=0, verbose_name='Precio Venta CLP')
    precio_venta_uf = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Precio Venta UF')
    precio_arriendo_clp = models.BigIntegerField(default=0, verbose_name='Precio Arriendo CLP')
    precio_arriendo_uf = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Precio Arriendo UF')

    # Ubicación
    region = models.CharField(max_length=100, verbose_name='Región')
    comuna = models.CharField(max_length=100, verbose_name='Comuna')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'
        ordering = ['-fecha_publicacion', '-id']

    def __str__(self):
        return f"{self.get_tipo_propiedad_display()} en {self.comuna} ({self.codigo or self.id})"


class PropiedadImagen(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='imagenes')
    nombre_archivo = models.CharField(max_length=255)
    ruta_archivo = models.CharField(max_length=1024) # Ruta relativa para usar en templates
    es_principal = models.BooleanField(default=False, verbose_name='Es Principal')
    orden = models.PositiveIntegerField(default=0)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Imagen de Propiedad'
        verbose_name_plural = 'Imágenes de Propiedad'
        ordering = ['orden', '-es_principal']

    def save(self, *args, **kwargs):
        # Ensure only one principal image
        if self.es_principal:
            PropiedadImagen.objects.filter(propiedad=self.propiedad, es_principal=True).exclude(pk=self.pk).update(es_principal=False)
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Imagen {self.id} de {self.propiedad}"
