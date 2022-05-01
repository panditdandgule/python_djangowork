from django.urls import path
from testapp import views

urlpatterns = [
    path(r'^api/$', views.EmployeeCRUDCBV.as_view()),

]
