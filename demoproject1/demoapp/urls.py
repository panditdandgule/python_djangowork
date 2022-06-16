from django.urls import path
from demoapp import views

urlpatterns = [
    path('stud/', views.student_data),
]
