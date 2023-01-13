from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('about', views.AboutView.as_view(), name="about"),
    path('service', views.ServiceView.as_view(), name="service"),
    path('gallery', views.GalleryView.as_view(), name="gallery"),
    path('contact', views.ContactView.as_view(), name="contact"),
    # path('booking', views.BookingView.as_view(), name="booking"),
    path('volume', views.VolumetricWeightView.as_view(), name="volume"),
    path('booking', views.new_booking, name="booking"),
    path('booking_list', views.BookingView.as_view(), name="booking-list"),
    path('booking_detail/<str:pk>', views.BookingDetailView.as_view(), name='booking-detail'),
    path('new_office', views.new_office, name="new-office"),
    path('office_list', views.OfficeView.as_view(), name="office-list"),
    path('office_update/<str:pk>', views.OfficeUpdateView.as_view(), name='update-office'),
    path('office_delete/<int:id>', views.office_delete, name="office-delete"),
]