from django.urls import path
from . import views

urlpatterns = [
    path('all-courier', views.AllCourierListView.as_view(), name="all-couriers"),
    path('add-new-courier', views.add_new_couriers, name="add-new-courier"),
    path('update-courier/<int:pk>', views.CourierUpdateView.as_view(), name='update_courier'),
    path('all-origin', views.AllOriginListView.as_view(), name="all-origins"),
    path('add-new-origin', views.add_new_origin, name="add-new-origin"),
    path('update-origin/<int:pk>', views.OriginUpdateView.as_view(), name='update_origin'),
    path('all-destination', views.AllDestinationListView.as_view(), name="all-destinations"),
    path('add-new-destination', views.add_new_destination, name="add-new-destination"),
    path('update-destination/<int:pk>', views.DestinationUpdateView.as_view(), name='update_destination'),
    path('all-shipper', views.AllShipperListView.as_view(), name="all-shippers"),
    path('add-new-shipper', views.add_new_shipper, name="add-new-shipper"),
    path('update-shipper/<int:pk>', views.ShipperUpdateView.as_view(), name='update_shipper'),
    path('all-receiver', views.AllReceiverListView.as_view(), name="all-receivers"),
    path('add-new-receiver', views.add_new_receiver, name="add-new-receiver"),
    path('update-receiver/<int:pk>', views.ReceiverUpdateView.as_view(), name='update_receiver'),
]