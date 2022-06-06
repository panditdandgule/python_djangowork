from django.urls import path
from .views import welcome_page,list_employee,save_employee,edit_employee,delete_employee

urlpatterns = [
    path('',welcome_page),
    path('show/',list_employee),
    path('save/',save_employee),
    path('edit/<int:eid>',edit_employee),
    path('delete/<int:eid>',delete_employee),
]
