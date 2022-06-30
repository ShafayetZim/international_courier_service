from django.urls import path
from . import views

urlpatterns = [
    path('all-courier', views.AllCourierListView.as_view(), name="all-couriers"),
    path('add-new-courier', views.add_new_couriers, name="add-new-courier"),
    path('update-courier/<int:pk>', views.CourierUpdateView.as_view(), name='update_courier'),
    path('courier-delete/<int:id>', views.courier_delete, name="courier-delete"),
    path('all-origin', views.AllOriginListView.as_view(), name="all-origins"),
    path('add-new-origin', views.add_new_origin, name="add-new-origin"),
    path('update-origin/<int:pk>', views.OriginUpdateView.as_view(), name='update_origin'),
    path('origin-delete/<int:id>', views.origin_delete, name="origin-delete"),
    path('all-destination', views.AllDestinationListView.as_view(), name="all-destinations"),
    path('add-new-destination', views.add_new_destination, name="add-new-destination"),
    path('update-destination/<int:pk>', views.DestinationUpdateView.as_view(), name='update_destination'),
    path('destination-delete/<int:id>', views.destination_delete, name="destination-delete"),
    path('all-extra', views.AllExtraListView.as_view(), name="all-extras"),
    path('sales-delete/<int:id>', views.sales_delete, name="sales-delete")
    
]