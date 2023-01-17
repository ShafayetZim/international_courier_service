from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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

    path('service_list', views.ServiceList.as_view(), name="service-list"),
    path('new_service', views.new_service, name="new-service"),
    path('gallery_list', views.GalleryList.as_view(), name="gallery-list"),
    path('new_gallery', views.new_gallery, name="new-gallery"),
    path('partner_list', views.PartnerList.as_view(), name="partner-list"),
    path('new_partner', views.new_partner, name="new-partner"),
    path('review_list', views.ReviewList.as_view(), name="review-list"),
    path('new_review', views.new_review, name="new-review"),
    path('facility_list', views.FacilityList.as_view(), name="facility-list"),
    path('new_facility', views.new_facility, name="new-facility"),
    path('benefit_list', views.BenefitList.as_view(), name="benefit-list"),
    path('new_benefit', views.new_benefit, name="new-benefit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)