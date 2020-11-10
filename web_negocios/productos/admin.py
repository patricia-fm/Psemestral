from django.contrib import admin

# Register your models here.
from .models import producto 

class ProductoAdmin(admin.ModelAdmin):
    #Agregar restricciones del adminstrador
    readonly_fields = ('created', 'updated')
#Registra el modelo para ser administrado
admin.site.register(producto,ProductoAdmin)
