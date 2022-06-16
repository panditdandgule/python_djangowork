from django.urls import path
from sessionapp import views

urlpatterns = [
    path('scookie/',views.setcookie),
    path('gcookie/',views.getcookie),

]
