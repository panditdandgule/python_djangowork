from django.urls import path
from formapp import views
urlpatterns = [
    path('app/', views.feedbackview),
]
