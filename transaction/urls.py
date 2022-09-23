from django.urls import path
from . import views
from django import forms
from transaction.forms import ShipmentCreateForm
from transaction.preview import TransactionFormPreview

urlpatterns = [
    path('new-shipper', views.new_shipper, name="new-shipper"),
    path('all-shipper', views.AllShipperListView.as_view(), name="all-shippers"),
    path('update-shipper/<str:pk>', views.ShipperUpdateView.as_view(), name='update_shipper'),
    path('shipper-delete/<str:shipper_code>', views.shipper_delete, name="shipper-delete"),
    path('detail-shipper/<str:pk>', views.ShipperDetailView.as_view(), name='detail_shipper'),
    path('new-receiver', views.new_receiver, name="new-receiver"),
    path('all-receiver', views.AllReceiverListView.as_view(), name="all-receivers"),
    path('update-receiver/<str:pk>', views.ReceiverUpdateView.as_view(), name='update_receiver'),
    path('receiver-delete/<str:receiver_code>', views.receiver_delete, name="receiver-delete"),
    path('detail-receiver/<str:pk>', views.ReceiverDetailView.as_view(), name='detail_receiver'),
    path('new-shipment', views.new_shipment, name="new-shipment"),
    path('all-shipment', views.AllShipmentListView.as_view(), name="all-shipments"),
    path('detail-shipment/<str:pk>', views.ShipmentDetailView.as_view(), name='detail_shipment'),
    path('shipment-delete/<str:shipment_no>', views.shipment_delete, name="shipment-delete"),
    path('shipment-edit/<str:shipment_no>', views.shipment_edit, name="shipment-edit"),
    path('shipping-status/<str:pk>', views.ShippingStatus.as_view(), name="shipping-status"),
    path('update-shipment/<str:pk>', views.ShipmentUpdateView.as_view(), name='update_shipment'),
    path('shipper-information', views.shipper_info, name="shipper-information"),
    path('receiver-information', views.receiver_info, name="receiver-information"),
    path('print-invoice/<str:shipment_no>', views.print_invoice, name='print-invoice'),
    path('airway-bill/<str:shipment_no>', views.airway_bill, name='airway-bill'),
    path('money-receipt/<str:shipment_no>', views.money_receipt, name='money-receipt'),
    path('details/<str:pk>', views.DetailView.as_view(), name='details'),
    # path('post/', TransactionFormPreview(ShipmentCreateForm)),
]