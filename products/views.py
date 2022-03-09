
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse_lazy
from .models import Products

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib import messages

from .form import ProductForm, RowProductForm, UserForm





def base(request):
    username = request.COOKIES['username']
    content = {
        'username':username
    }
    return  render(request, 'base.html', content)
   
    return resp    

@login_required(login_url='login')
def product_list(request, *args, **kwargs):
    """
        This function display list of all the product and credential of the user as cookies 
    """
    
    product = Products.objects.all()
    number_visit = request.session.get('visit', 0) + 1
    request.session['visit'] = number_visit
    if number_visit>4:
        del(request.session['visit'])
    context = {
        'products':product,
        'number':number_visit
    }
    resp = render(request, 'products/list.html', context)
    username = request.user.username 
    password = request.user.password
    resp.set_cookie('username',username)
    resp.set_cookie('password',password)
    return resp

def test_email(request):
    if request.user.email.endswith('@donald.com'):
        return 
      



def register(request):
    form = UserForm()
    if request.method == 'POST':
        form =UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre conpte a ete bien creer")
            return redirect('login')
        else:
            messages.error(request, form.errors)    
    return render(request, 'products/register.html', {'form':form})


def connexion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenue')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:    
                return redirect('/')
        else:
            messages.error(request, "erreur d'authentification ")    
    return render(request, 'products/login.html')


@login_required()
def deconnection(request):
    logout(request)
    return redirect('login')






@login_required
def productCreate(request):
    form = ProductForm(request.POST or None)
    messages = ''
    if form.is_valid():
        form.save()
        form = ProductForm()
        messages = "We have receive your product"
    return render(request, 'products/create.html', {'form':form, 'message':messages}) 

@login_required
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

@login_required(login_url='login')
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