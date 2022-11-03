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
]