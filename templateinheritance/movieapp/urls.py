from django.urls import path
from movieapp import views

urlpatterns = [
    path('temp/', views.home),
]
