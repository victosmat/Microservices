from django.urls import path
from . import views

urlpatterns = [
    path("shipment_status/", views.shipment_status, name="shipment_status"),
    path("shipment_updates/", views.shipment_reg_update, name="shipment_updates"),
]
