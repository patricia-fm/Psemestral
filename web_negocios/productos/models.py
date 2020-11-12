from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class producto(models.Model):
    titulo = models.CharField(max_length=50, verbose_name="Titulo del Producto")
    descripcion = RichTextField(verbose_name="Detalle del producto")
    imagen = models.ImageField(upload_to='productos', verbose_name="Imagen del producto")
    precio = models.IntegerField(verbose_name="Precio del producto")
    estaEnOferta = models.BooleanField(verbose_name="Esta en Oferta?", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.titulo
