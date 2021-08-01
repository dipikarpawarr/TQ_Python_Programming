from Student import views
from django.urls import path

urlpatterns = [
    path('form', views.StudentView),
    path('dashboard', views.StudentDashboard),
]