from django.urls import path
from employee.views import welcome_page, save_employee, edit_employee, delete_employee, list_employees

urlpatterns = [
    path('', welcome_page, name='welcome'),
    path('save/', save_employee),  # function ref--- dont call the function here..
    path('edit/<int:eid>', edit_employee),  # http:localhost:8000/employee/edit
    path('delete/<int:eid>', delete_employee),  # http://localhost:8000/employee/delete
    path('show/', list_employees),
]
