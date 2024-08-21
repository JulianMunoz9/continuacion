from django import forms
from .models import Producto, Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm     #formulario de creacion de usuarios

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion','precio', 'stock']

    #validacion personalizada para el campo de precio
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:     #con esta validacion nos aseguramos que aparezca un error si el precio es menor a cero.
            raise forms.ValidationError('usted que piensa de la vida colocando precios en negativo? ')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock <= 0:
            raise forms.ValidationError('Como vas a vender lo que no tienes?')
        return stock

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']