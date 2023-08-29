from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Registra los modelos en el panel de administración

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad', 'pais')
    # Puedes personalizar más opciones aquí, como list_filter, search_fields, etc.

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'especialidad')
    list_filter = ('laboratorio',)
    search_fields = ('nombre',)
    # Puedes personalizar más opciones aquí, como list_editable, date_hierarchy, etc.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('laboratorio',)
    search_fields = ('nombre', 'laboratorio__nombre')
    # Puedes personalizar más opciones aquí, como list_editable, date_hierarchy, etc.

