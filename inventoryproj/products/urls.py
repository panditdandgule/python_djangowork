from django.urls import path
from .views import welcome_page,save_products,list_products,delete_product

urlpatterns = [
    path('', welcome_page),
    path('save/',save_products),
    path('show/',list_products),
    path('delete/<int:pid>',delete_product),

]
