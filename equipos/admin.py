from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'fecha_ingreso', 'ubicacion')
    list_filter = ('estado', 'categoria')
    search_fields = ('nombre', 'categoria', 'ubicacion')
