from django.contrib import admin


# Register your models here.
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Laboratorio, LaboratorioAdmin)

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    ordering = ('nombre',)

admin.site.register(DirectorGeneral, DirectorGeneralAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio',
        'f_fabricacion_year', 'p_costo', 'p_venta')
    
    ordering = ('nombre', 'laboratorio')

    list_display_links = ('nombre', 'laboratorio')

    list_filter = ('nombre', 'laboratorio')
    
    def f_fabricacion_year(self, obj):
        return obj.f_fabricacion.year
    
    f_fabricacion_year.short_description = "F Fabricacion"

admin.site.register(Producto, ProductoAdmin) 
