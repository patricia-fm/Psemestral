from django import forms

class RegisterForm(forms.Form):
    nombre_dueño = forms.CharField(label="Su nombre", required=True, min_length=3,
    max_length=50, widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese su nombre'}))
    nombre_negocio = forms.CharField(label="Nombre del negocio", required=True, min_length=3, max_length=100,
    widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese nombre de su negocio'}))
    producto = forms.CharField(label="Nombre del producto", required=True, min_length=3, max_length=100,
    widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese nombre del producto'}))
    direccion = forms.CharField(label="Direccion del negocio", required=True, min_length=5, max_length=100,
    widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese direccion de su negocio'}))
    telefono = forms.IntegerField(label="Telefono de contacto", required=True,
    widget=forms.NumberInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese telefono de contacto'}))
    descripcion = forms.CharField(label="Descripcion del negocio y producto", required=True, min_length=10, 
    max_length=1000, widget=forms.Textarea(attrs={'class':'form-control mb-3','placeholder':'Ingrese descripcion','rows':3}))
