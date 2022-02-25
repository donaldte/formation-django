from unicodedata import name
from django.urls import path, include
from products.views import connexion, deconnection, deleteProduct, modifier, product_list, productCreate, register, table
from django.contrib.auth import views


urlpatterns = [
    path('', product_list, name='home'),
    path('create', productCreate, name='create'),
    path('update/<int:my_id>', modifier, name='update'),
    path('delete/<int:my_id>', deleteProduct, name='delete'),
    path('mamager', table, name='table'),
    path('register', register, name='register' ),
    path('login', connexion, name='login'),
    path('logout', deconnection, name='logout'),

    path('reset_password', views.PasswordResetView.as_view(template_name='products/password_reset.html'), name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(template_name="products/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name="products/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name="products/password_reset_done.html"), name="password_reset_complete")

]