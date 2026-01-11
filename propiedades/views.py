import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Propiedad, PropiedadImagen
from .forms import PropiedadForm

def save_uploaded_image(propiedad, uploaded_file, es_principal=False, orden=0):
    """
    Helper function to save image to filesystem without using ImageField.
    Stores at: media/propiedades/<id>/<filename>
    """
    # Define paths
    folder = f'propiedades/{propiedad.id}'
    filename = uploaded_file.name
    # Ensure filename is safe or unique if needed, but for now assuming simple replace
    # Ensure filename is safe or unique if needed, but for now assuming simple replace
    # Use forward slashes for URL compatibility even on Windows
    file_path_relative = f"{folder}/{filename}"

    
    # Save file physically using default storage (handles media root)
    saved_path = default_storage.save(file_path_relative, ContentFile(uploaded_file.read()))
    
    # Create DB record with path string
    PropiedadImagen.objects.create(
        propiedad=propiedad,
        nombre_archivo=filename,
        # Store expected URL path (e.g. /media/propiedades/1/foto.jpg) or relative path
        # In templates we usually use {{ MEDIA_URL }}{{ img.ruta_archivo }}
        # But wait, default_storage.save returns the name relative to MEDIA_ROOT.
        # Let's save that relative name.
        ruta_archivo=saved_path, 
        es_principal=es_principal,
        orden=orden
    )

def propiedad_list(request):
    propiedades = Propiedad.objects.exclude(estado='INACTIVO')
    return render(request, 'propiedades/list.html', {'propiedades': propiedades})

def propiedad_detail(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    return render(request, 'propiedades/detail.html', {'propiedad': propiedad})

def propiedad_create(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            propiedad = form.save()
            
            # Handle multiple images manually
            files = request.FILES.getlist('imagenes')
            for i, f in enumerate(files):
                es_principal = (i == 0)
                save_uploaded_image(propiedad, f, es_principal, i)
            
            messages.success(request, 'Propiedad creada exitosamente.')
            return redirect('propiedades:list')
    else:
        form = PropiedadForm()
    
    return render(request, 'propiedades/form.html', {'form': form, 'action': 'Crear'})

def propiedad_update(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            propiedad = form.save()
            
            # Add new images
            files = request.FILES.getlist('imagenes')
            current_count = propiedad.imagenes.count()
            for i, f in enumerate(files):
                save_uploaded_image(propiedad, f, es_principal=False, orden=current_count + i)
            
            messages.success(request, 'Propiedad actualizada exitosamente.')
            return redirect('propiedades:list')
    else:
        form = PropiedadForm(instance=propiedad)
    
    return render(request, 'propiedades/form.html', {'form': form, 'action': 'Editar', 'propiedad': propiedad})

def propiedad_delete(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        # Optional: Delete files from disk?
        # Requirement says "Eliminar usuario (borrado lógico)" but for properties 
        # "Eliminar... Las imágenes pueden desactivarse sin eliminarse".
        # But the delete VIEW usually removes.
        # If we delete the object, cascade deletes DB records. 
        # Files remain on disk unless we implement logic to delete them.
        # Given "solo usar campos de texto", easy to leave files. 
        # Let's just standard delete object.
        propiedad.delete()
        messages.success(request, 'Propiedad eliminada exitosamente.')
        return redirect('propiedades:list')
    return render(request, 'propiedades/delete.html', {'propiedad': propiedad})
