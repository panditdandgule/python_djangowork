from django.urls import path
from demoapp import views

urlpatterns = [
    path('demo/', views.home),
    path('stud/',views.studentinputview)
]
