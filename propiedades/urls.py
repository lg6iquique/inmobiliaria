from django.urls import path
from . import views

app_name = 'propiedades'

urlpatterns = [
    path('', views.propiedad_list, name='list'),
    path('crear/', views.propiedad_create, name='create'),
    path('<int:pk>/', views.propiedad_detail, name='detail'),
    path('<int:pk>/editar/', views.propiedad_update, name='update'),
    path('<int:pk>/eliminar/', views.propiedad_delete, name='delete'),
]
