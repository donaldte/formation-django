from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder':'votre nom ici',
        }
    ))
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'placeholder':'Enter product description',
            'rows':5,
            'cols':10,
            'class':'m1 m2 m3',
            'id':'my_id',
        }
    ))
    price = forms.DecimalField(label='', initial=10)
    # image = forms.ImageField()
    slug = forms.SlugField(label='', widget=forms.TextInput( attrs={'placeholder':'slug here'}))
    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'image', 'slug',)


    

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("com"):
            raise forms.ValidationError("l'email doit acheve avec .com")            

  
       



















class RowProductForm(forms.Form):
    name = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={
            'placeholder':'votre nom ici',
        }
    ))
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            'placeholder':'Enter product description',
            'rows':5,
            'cols':10,
            'class':'m1 m2 m3',
            'id':'my_id',
        }
    ))
    price = forms.DecimalField(label='', initial=10)
    # image = forms.ImageField()
    slug = forms.CharField(label='')       