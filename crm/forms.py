from django import forms
from .models import Client, Product, Purchase


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['client', 'product', 'quantity']
