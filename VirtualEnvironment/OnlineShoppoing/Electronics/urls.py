from Electronics import views
from django.urls import path
import Electronics

urlpatterns = [
    path("items",views.eleShow),
    path("items/computer", views.compShow),
    path("items/homeappliances", views.homeAppliancesDetails)
]