from django.urls import path
from modelformapp import views

urlpatterns = [
    path('test/',views.student_view),
]
