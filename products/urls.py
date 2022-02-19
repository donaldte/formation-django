from django.urls import path
from products.views import deleteProduct, modifier, product_list, productCreate, table


urlpatterns = [
    path('', product_list, name='home'),
    path('create', productCreate, name='create'),
    path('update/<int:my_id>', modifier, name='update'),
    path('delete/<int:my_id>', deleteProduct, name='delete'),
    path('mamager', table, name='table'),
]