from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioChangeForm

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/lista.html'
    context_object_name = 'usuarios'
    ordering = ['-fecha_creacion']

    def get_queryset(self):
        # We might want to show inactive users too, or filter them. 
        # Requirement: "Eliminar usuario (borrado lógico)".
        # Usually admins want to see all, but let's show all for now to verify logic.
        return Usuario.objects.all()

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/detalle.html'
    context_object_name = 'usuario'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'usuarios/formulario.html'
    success_url = reverse_lazy('usuarios:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario creado exitosamente.')
        return super().form_valid(form)

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioChangeForm
    template_name = 'usuarios/formulario.html'
    success_url = reverse_lazy('usuarios:lista')

    def form_valid(self, form):
        messages.success(self.request, 'Usuario actualizado exitosamente.')
        return super().form_valid(form)

class UsuarioDeleteView(View):
    """
    View to handle logical deletion.
    GET: Show confirmation
    POST: Perform logical delete
    """
    template_name = 'usuarios/eliminar.html'
    success_url = reverse_lazy('usuarios:lista')

    def get(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        return render(request, self.template_name, {'usuario': usuario})

    def post(self, request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        usuario.is_active = False
        usuario.save()
        messages.success(request, f'Usuario {usuario.username} desactivado exitosamente.')
        return redirect(self.success_url)
