from django.urls import path
from .views import welcome_page,add_employee,list_employee,delete_employee,edit_employee

urlpatterns = [
    path('', welcome_page),
    path('show/',list_employee)
]
