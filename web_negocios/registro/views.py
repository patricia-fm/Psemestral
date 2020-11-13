from django.shortcuts import render, get_object_or_404
from .forms import RegisterForm

# Create your views here.

def registro(request):
    registro = RegisterForm()
    if request.method == "POST":
        registro = RegisterForm(data=request.POST)
        if registro.is_valid():
            nombre_dueño = request.POST.get("nombre_dueño",'')
            nombre_negocio = request.POST.get("nombre_negocio",'')
            producto = request.POST.get("producto",'')
            direccion = request.POST.get("direccion",'')
            telefono = request.POST.get("telefono",'')
            descripcion = request.POST.get("descripcion",'')
    return render(request, "registro.html", {'form': registro})

def detalleRegistro(request, prod_id):
    #dregistro = get_object_or_404(registro, id=reg_id)
    dregistro = registro.objects.get(id=reg_id)
    return render(request, "ver_registro.html", {'registro': dregistro})
