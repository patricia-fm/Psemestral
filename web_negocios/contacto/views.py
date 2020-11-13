from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contacto(request):
    formulario = ContactForm()
    if request.method == "POST":
        print(request.POST)
    return render(request, "contacto.html", {'form':formulario})
