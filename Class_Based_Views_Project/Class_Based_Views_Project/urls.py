"""Class_Based_Views_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.StudentList_View.as_view(), name='students'),
    path('<int:pk>', views.StudentDetails_View.as_view(), name='details'),
    path('createStudent/', views.StudentCreate_View.as_view()),
    path('updateStudent/<int:pk>', views.StudentUpdate_View.as_view()),
    path('deleteStudent/<int:pk>', views.StudentDelete_View.as_view()),
]
