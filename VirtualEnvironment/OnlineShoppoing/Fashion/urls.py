from Fashion import views
from django.urls import path

urlpatterns = [
    path("items", views.fashionData),
    path("items/cloths", views.clothsDetails),
    path("items/footwear", views.footwearDetails),
    path("items/cosmatics", views.consmaticDetails),
]