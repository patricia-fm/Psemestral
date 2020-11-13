from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.

def contacto(request):
    formulario = ContactForm()
    if request.method == "POST":
        
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre','')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')
            email = EmailMessage("Le han contactado!", "{} {}: dijo {}".format(nombre,correo,mensaje),
            "encuentranegocio@gmail.com",
            ['encuentranegocio@gmail.com'],
            reply_to=[correo])
            try:
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except Exception as e:
                return redirect(reverse('contacto')+ "?ok")
    return render(request, "contacto.html", {'form':formulario})
