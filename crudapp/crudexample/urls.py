
from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show',views.show),
    path('edit/<int:eid>', views.edit),
    path('update/<int:eid>', views.update),
    path('delete/<int:eid>', views.destroy),
]
