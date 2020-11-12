from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html", {'titulo': 'Ofrece aquí tus productos'})

def contacto(request):
    return render(request,"contacto.html")
