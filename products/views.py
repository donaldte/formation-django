from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse_lazy
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

def modifier(request, my_id):
    obj = get_object_or_404(Products, id=my_id)
    # try:
    #     obj = Products.objects.get(id=my_id)
    # except Products.DoesNotExist:
    #     raise Http404     
    form = ProductForm(request.POST or None, instance=obj)
    messages = ''
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "Your modification was successfully done!"
    return render(request, 'products/update.html', {'form':form, 'message':messages}) 

def table(request):
    obj = Products.objects.all()
    return render(request, 'products/table.html', {'obj':obj})


def deleteProduct(request, my_id):
    obj = get_object_or_404(Products, id=my_id)
    name = obj.name
    if request.method == "POST":
        obj.delete()
        return redirect('table')

    return render(request, 'products/delete.html',{"name":name})    


    






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