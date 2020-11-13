from django import forms 

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Su nombre", required=True, min_length=3, max_length=100)
    correo = forms.EmailField(label="Su correo", required=True)
    mensaje = forms.CharField(label="Su mensaje", required=True, min_length=10, max_length=1000)

