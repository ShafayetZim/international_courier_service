from django.urls import path
from . import views

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
    path('new-sales', views.new_sales, name="new-sales"),
    path('shipper-information', views.shipper_info, name="shipper-information"),
    path('receiver-information', views.receiver_info, name="receiver-information"),
]