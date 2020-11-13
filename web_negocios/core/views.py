from django.shortcuts import render
from productos.models import producto

# Create your views here.
def home(request):
    productos = producto.objects.all()
    return render(request,"index.html", {'titulo': 'Ofrece aquí tus productos'
    ,'productos': productos })


