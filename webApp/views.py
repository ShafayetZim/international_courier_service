from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DetailView
from django.views import View
from .forms import *
from .models import *
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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
            'pageview': "Contact",
            'office': Office.objects.all(),
        }
        return render(request, 'web/contact.html', context)


# class BookingView(View):
#     def get(self, request):
#         context = {
#             'title': "Booking",
#             'pageview': "Online Booking"
#         }
#         return render(request, 'web/booking.html', context)


class VolumetricWeightView(View):
    def get(self, request):
        context = {
            'title': "Volume",
            'pageview': "Volumetric Weight"
        }
        return render(request, 'web/volume.html', context)


def new_booking(request):
    template_name = 'web/booking.html'

    if request.method == 'GET':
        print("GET called")
        booking_form = BookingCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        booking_form = BookingCreateForm(request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.author = request.user
            booking.is_active = True
            booking.save()

            messages.add_message(request, messages.SUCCESS, 'New Booking Entry Successful')
            return redirect('booking')

            # def get_absolute_url(self):
            #     return reverse('shipment-edit', kwargs={'pk': self.pk})

        else:
            print("Not Valid Create Form")
            print(booking_form.errors)

    return render(request, template_name, {
        'booking_form': booking_form,
        'title': 'Booking',
        'nav_bar': 'new_booking',
    })


class BookingView(ListView):
    model = Booking
    template_name = 'web/booking_list.html'
    context_object_name = 'booking'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Booking List"
        context["nav_bar"] = "booking_list"
        context['booking'] = self.model.objects.all().order_by('-id')
        return context


class BookingDetailView(DetailView):
    model = Booking
    template_name = 'web/booking_detail.html'
    context_object_name = 'booking'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Booking Information"
        context["nav_bar"] = "booking_list"
        return context


class OfficeView(ListView):
    model = Office
    template_name = 'web/office_list.html'
    context_object_name = 'office'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Office List"
        context["nav_bar"] = "office_list"
        context['office'] = self.model.objects.all().order_by('-id')
        return context


def new_office(request):
    template_name = 'web/new_office.html'

    if request.method == 'GET':
        print("GET called")
        office_form = OfficeCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        office_form = OfficeCreateForm(request.POST)

        if office_form.is_valid():
            office = office_form.save(commit=False)
            office.author = request.user
            office.is_active = True
            office.save()

            messages.add_message(request, messages.SUCCESS, 'New Office Entry Successful')
            return redirect('office-list')

            # def get_absolute_url(self):
            #     return reverse('shipment-edit', kwargs={'pk': self.pk})

        else:
            print("Not Valid Create Form")
            print(office_form.errors)

    return render(request, template_name, {
        'office_form': office_form,
        'title': 'Office',
        'nav_bar': 'new_office',
    })


class OfficeUpdateView(SuccessMessageMixin, UpdateView):
    model = Office
    form_class = OfficeCreateForm
    success_url = reverse_lazy('office-list')
    template_name = 'web/update_office.html'
    success_message = "Office was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Office Information"
        context["nav_bar"] = "office_list"
        return context


def office_delete(request, id):
    if request.method == 'GET':
        instance = Office.objects.get(id=id)
        Office.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('office-list')


class ServiceList(ListView):
    model = Service
    template_name = 'web_data/service_list.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Service List"
        context["nav_bar"] = "service_list"
        context['service'] = self.model.objects.all().order_by('-id')
        return context


def new_service(request):
    template_name = 'web_data/new_service.html'

    if request.method == 'GET':
        print("GET called")
        service_form = ServiceCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        service_form = ServiceCreateForm(request.POST)

        if service_form.is_valid():
            booking = service_form.save(commit=False)
            booking.save()

            messages.add_message(request, messages.SUCCESS, 'New Service Entry Successful')
            return redirect('service-list')

        else:
            print("Not Valid Create Form")
            print(service_form.errors)

    return render(request, template_name, {
        'service_form': service_form,
        'title': 'New Service',
        'nav_bar': 'new_service',
    })


class GalleryList(ListView):
    model = Gallery
    template_name = 'web_data/gallery_list.html'
    context_object_name = 'office'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Office List"
        context["nav_bar"] = "office_list"
        context['office'] = self.model.objects.all().order_by('-id')
        return context


def new_gallery(request):
    template_name = 'web_data/new_gallery.html'

    if request.method == 'GET':
        print("GET called")
        gallery_form = GalleryCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        gallery_form = GalleryCreateForm(request.POST)

        if gallery_form.is_valid():
            gallery = gallery_form.save(commit=False)
            gallery.save()

            messages.add_message(request, messages.SUCCESS, 'New Gallery Entry Successful')
            return redirect('gallery-list')

        else:
            print("Not Valid Create Form")
            print(gallery_form.errors)

    return render(request, template_name, {
        'gallery_form': gallery_form,
        'title': 'New Gallery',
        'nav_bar': 'new_gallery',
    })


class PartnerList(ListView):
    model = Partner
    template_name = 'web_data/partner_list.html'
    context_object_name = 'partner'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Partner List"
        context["nav_bar"] = "partner_list"
        context['partner'] = self.model.objects.all().order_by('-id')
        return context


def new_partner(request):
    template_name = 'web_data/new_partner.html'

    if request.method == 'GET':
        print("GET called")
        partner_form = PartnerCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        partner_form = PartnerCreateForm(request.POST)

        if partner_form.is_valid():
            partner = partner_form.save(commit=False)
            partner.save()

            messages.add_message(request, messages.SUCCESS, 'New Partner Entry Successful')
            return redirect('partner-list')

        else:
            print("Not Valid Create Form")
            print(partner_form.errors)

    return render(request, template_name, {
        'partner_form': partner_form,
        'title': 'New Partner',
        'nav_bar': 'new_partner',
    })


class ReviewList(ListView):
    model = Review
    template_name = 'web_data/review_list.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Review List"
        context["nav_bar"] = "Review_list"
        context['review'] = self.model.objects.all().order_by('-id')
        return context


def new_review(request):
    template_name = 'web_data/new_review.html'

    if request.method == 'GET':
        print("GET called")
        review_form = ReviewCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        review_form = ReviewCreateForm(request.POST, request.FILES)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.save()

            messages.add_message(request, messages.SUCCESS, 'New Review Entry Successful')
            return redirect('review-list')

        else:
            print("Not Valid Create Form")
            print(review_form.errors)

    return render(request, template_name, {
        'review_form': review_form,
        'title': 'New Review',
        'nav_bar': 'new_review',
    })


class FacilityList(ListView):
    model = Facility
    template_name = 'web_data/facility_list.html'
    context_object_name = 'office'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Facility List"
        context["nav_bar"] = "facility_list"
        context['facility'] = self.model.objects.all().order_by('-id')
        return context


def new_facility(request):
    template_name = 'web_data/new_facility.html'

    if request.method == 'GET':
        print("GET called")
        facility_form = FacilityCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        facility_form = FacilityCreateForm(request.POST)

        if facility_form.is_valid():
            facility = facility_form.save(commit=False)
            facility.save()

            messages.add_message(request, messages.SUCCESS, 'New Facility Entry Successful')
            return redirect('facility-list')

        else:
            print("Not Valid Create Form")
            print(facility_form.errors)

    return render(request, template_name, {
        'facility_form': facility_form,
        'title': 'New Facility',
        'nav_bar': 'new_facility',
    })


class BenefitList(ListView):
    model = Benefit
    template_name = 'web_data/benefit_list.html'
    context_object_name = 'benefit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Benefit List"
        context["nav_bar"] = "benefit_list"
        context['benefit'] = self.model.objects.all().order_by('-id')
        return context


def new_benefit(request):
    template_name = 'web_data/new_benefit.html'

    if request.method == 'GET':
        print("GET called")
        benefit_form = BenefitCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        benefit_form = BenefitCreateForm(request.POST)

        if benefit_form.is_valid():
            benefit = benefit_form.save(commit=False)
            benefit.save()

            messages.add_message(request, messages.SUCCESS, 'New Benefit Entry Successful')
            return redirect('benefit-list')

        else:
            print("Not Valid Create Form")
            print(benefit_form.errors)

    return render(request, template_name, {
        'benefit_form': benefit_form,
        'title': 'New Benefit',
        'nav_bar': 'new_benefit',
    })