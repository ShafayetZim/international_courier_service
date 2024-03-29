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
    path('service_update/<str:pk>', views.ServiceUpdateView.as_view(), name='update-service'),
    path('new_service', views.new_service, name="new-service"),
    path('service_delete/<int:id>', views.service_delete, name="service-delete"),
    path('gallery_list', views.GalleryList.as_view(), name="gallery-list"),
    path('new_gallery', views.new_gallery, name="new-gallery"),
    path('gallery_delete/<int:id>', views.gallery_delete, name="gallery-delete"),
    path('partner_list', views.PartnerList.as_view(), name="partner-list"),
    path('new_partner', views.new_partner, name="new-partner"),
    path('partner_delete/<int:id>', views.partner_delete, name="partner-delete"),
    path('review_list', views.ReviewList.as_view(), name="review-list"),
    path('review_update/<str:pk>', views.ReviewUpdateView.as_view(), name="update-review"),
    path('review_delete/<int:id>', views.review_delete, name="review-delete"),
    path('new_review', views.new_review, name="new-review"),
    path('facility_list', views.FacilityList.as_view(), name="facility-list"),
    path('facility_update/<str:pk>', views.FacilityUpdateView.as_view(), name='update-facility'),
    path('new_facility', views.new_facility, name="new-facility"),
    path('facility_delete/<int:id>', views.facility_delete, name="facility-delete"),
    path('benefit_list', views.BenefitList.as_view(), name="benefit-list"),
    path('new_benefit', views.new_benefit, name="new-benefit"),
    path('benefit_update/<str:pk>', views.BenefitUpdateView.as_view(), name='update-benefit'),
    path('benefit_delete/<int:id>', views.benefit_delete, name="benefit-delete"),
    path('slider_list', views.SliderList.as_view(), name="slider-list"),
    path('new_slider', views.new_slider, name="new-slider"),
    path('slider_update/<str:pk>', views.SliderUpdateView.as_view(), name='update-slider'),
    path('slider_delete/<int:id>', views.slider_delete, name="slider-delete"),
    path('about_list', views.AboutList.as_view(), name="about-list"),
    path('about_update/<str:pk>', views.AboutUpdateView.as_view(), name='update-about'),
    path('cargo_list', views.CargoList.as_view(), name="cargo-list"),
    path('new_cargo', views.new_cargo, name="new-cargo"),
    path('cargo_update/<str:pk>', views.CargoUpdateView.as_view(), name='update-cargo'),
    path('cargo_delete/<int:id>', views.cargo_delete, name="cargo-delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
