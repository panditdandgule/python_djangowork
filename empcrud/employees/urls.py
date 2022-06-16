from django.urls import path
from employees import views

urlpatterns = [
    path('', views.index,name='index'),
    path('add/',views.add,name='add'),
    path('edit/<int:employee_id>/',views.edit,name='edit'),
    path('delete/<int:employee_id>/',views.delete,name='delete'),
    path('insert/',views.insert,name='insert'),
    path('update/<int:employee_id>/',views.update,name='update'),
]
