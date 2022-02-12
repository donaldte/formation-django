from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'image', 'slug',)


class RowProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    # image = forms.ImageField()
    slug = forms.CharField()       