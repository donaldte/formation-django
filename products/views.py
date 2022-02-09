from django.shortcuts import render
from .models import Products
from .form import ProductForm

def product_list(request, *args, **kwargs):
    product = Products.objects.all()
    context = {
        'products':product
    }
    return render(request, 'products/list.html', context)

def productCreate(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "We have receive your product"


    return render(request, 'products/create.html', {'form':form, 'message':messages})    



