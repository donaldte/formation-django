from django.shortcuts import render
from .models import Products
from .form import ProductForm, RowProductForm

def product_list(request, *args, **kwargs):
    product = Products.objects.all()
    context = {
        'products':product
    }
    return render(request, 'products/list.html', context)

def productCreate(request):
    form = ProductForm(request.POST or None)
    messages = ''
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "We have receive your product"
    return render(request, 'products/create.html', {'form':form, 'message':messages}) 


# def productCreate(request):
#     if request.method == "POST":    
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         image = request.POST.get('image')
#         slug = request.POST.get('slug')
#         newProduct = Products.objects.create(name=name, description=description, price=price, image=image, slug=slug)
#         newProduct.save()
#         message = "your product was saved successfully"
#     return render(request, 'products/create.html', {"message":message}) 

# def productCreate(request):
#     form = RowProductForm()
#     message = ''
#     if request.method == "POST":
#         form = RowProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             new = Products.objects.create(**form.cleaned_data)
#             new.save()
#             form = RowProductForm()
#             message = 'product was successfully saved'
#     return render(request, 'products/create.html', {'form':form, 'message':message})