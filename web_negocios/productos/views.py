from django.shortcuts import render
from .models import producto
# Create your views here.

def verProductos(request):
    productos = producto.objects.all()
    return render(request, "productos.html", {'productos': productos})
