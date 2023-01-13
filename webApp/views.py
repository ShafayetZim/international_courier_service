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