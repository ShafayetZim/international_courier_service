from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


class HomeView(View):
    def get(self, request):
        context = {
            # 'slider': Slider.objects.all(),
            # 'ps': ProductSlider.objects.all(),
            # 'description': HomeAbout.objects.all(),
            'title': "Index",
            'pageview': "Home"
        }
        return render(request, 'web/index.html', context)


class AboutView(View):
    def get(self, request):
        context = {
            'title': "About",
            'pageview': "About"
        }
        return render(request, 'web/about.html', context)


class ServiceView(View):
    def get(self, request):
        context = {
            'title': "Service",
            'pageview': "About"
        }
        return render(request, 'web/service.html', context)


class GalleryView(View):
    def get(self, request):
        context = {
            'title': "Gallery",
            'pageview': "Gallery"
        }
        return render(request, 'web/gallery.html', context)


class ContactView(View):
    def get(self, request):
        context = {
            'title': "Contact",
            'pageview': "Contact"
        }
        return render(request, 'web/contact.html', context)


class BookingView(View):
    def get(self, request):
        context = {
            'title': "Booking",
            'pageview': "Online Booking"
        }
        return render(request, 'web/booking.html', context)


class VolumetricWeightView(View):
    def get(self, request):
        context = {
            'title': "Volume",
            'pageview': "Volumetric Weight"
        }
        return render(request, 'web/volume.html', context)
