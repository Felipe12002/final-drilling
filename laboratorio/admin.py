from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.
admin.site.register(Laboratorio)
admin.site.register(DirectorGeneral)
admin.site.register(Producto)