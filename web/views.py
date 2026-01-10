from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Persona
from .forms import PersonaForm


def index(request):
    """Vista principal - Página de inicio."""
    return render(request, 'inicio.html')


def persona_list(request):
    """Lista todas las personas."""
    personas = Persona.objects.all()
    return render(request, 'web/persona_list.html', {'personas': personas})


def persona_create(request):
    """Crea una nueva persona."""
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = PersonaForm()
    return render(request, 'web/persona_form.html', {'form': form, 'action': 'Crear'})


def persona_detail(request, pk):
    """Muestra el detalle de una persona."""
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'web/persona_detail.html', {'persona': persona})


def persona_delete(request, pk):
    """Elimina una persona."""
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona_list')
    return render(request, 'web/persona_confirm_delete.html', {'persona': persona})
