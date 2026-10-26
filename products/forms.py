from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "product_type", "status", "intended_use"]
        widgets = {"intended_use": forms.Textarea(attrs={"rows": 4})}