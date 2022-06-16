from django.urls import path
from .views import welcome,add_employee,list_employee,update_employee,edit_employee,delete_employee

urlpatterns = [
    path('', welcome),
    path('save/',add_employee),
    path('list/',list_employee),
    path('update/<int:eid>',update_employee),
    path('edit/<int:eid>',edit_employee),
    path('delete/<int:eid>',delete_employee),
]
