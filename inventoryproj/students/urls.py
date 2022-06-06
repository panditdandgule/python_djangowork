from django.urls import path
from .views import welcome_page,save_students,list_students,delete_student,edit_student

urlpatterns = [
    path('', welcome_page),
    path('save/',save_students),
    path('show/',list_students),
    path('delete/<int:sid>',delete_student),
    path('edit/<int:sid>',edit_student),

]
