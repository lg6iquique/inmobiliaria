from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personas/', views.persona_list, name='persona_list'),
    path('personas/crear/', views.persona_create, name='persona_create'),
    path('personas/<int:pk>/', views.persona_detail, name='persona_detail'),
    path('personas/<int:pk>/eliminar/', views.persona_delete, name='persona_delete'),
]
