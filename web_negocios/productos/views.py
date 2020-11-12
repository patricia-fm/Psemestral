from django.shortcuts import render, get_object_or_404
from .models import producto
# Create your views here.

def verProductos(request):
    productos = producto.objects.all()
    return render(request, "productos.html", {'productos': productos})

def detalleProductos(request, prod_id):
    #producto = producto.objects.get(id=prod_id)
    producto = get_object_or_404(producto, id=prod_id)
    return render(request, "ver_producto.html", {'producto': producto})

