from django.shortcuts import render, redirect

from .models import Courier, Destination, Origin, Shipper
from .forms import CourierCreateForm, OriginCreateForm, DestinationCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView)

# Create your views here.

class AllCourierListView(ListView):
    model = Courier  # Model I want to Covert to List
    template_name = 'courier.html'  # Template Name
    context_object_name = 'courier'  # Change default name of objectList
    ordering = ['-id']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Courier List"
        context["nav_bar"] = "courier_list"
        context['courier'] = self.model.objects.all().order_by('-id')
        return context


def add_new_couriers(request):
    print("called")
    template_name = 'add_new_courier.html'

    if request.method == 'GET':
        print("called GET")
        courier_form = CourierCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        courier_form = CourierCreateForm(request.POST)

        if courier_form.is_valid():
            obj = courier_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Courier Added Successfully!')
            return redirect('all-couriers')

        else:
            print("Not Valid Create Form")
            print(courier_form.errors)

    return render(request, template_name, {
        'courier_form': courier_form,
        'title': 'Add New Courier',
        'nav_bar': 'add_new_courier',
    })


class CourierUpdateView(SuccessMessageMixin, UpdateView):
    model = Courier
    form_class = CourierCreateForm
    success_url = reverse_lazy('all-couriers')
    template_name = 'update_courier.html'
    success_message = "Courier was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Courier Information"
        context["nav_bar"] = "courier_list"
        return context


def courier_delete(request, id):
    if request.method == 'GET':
        instance = Courier.objects.get(id=id)
        Courier.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-couriers')


class AllOriginListView(ListView):
    model = Origin  # Model I want to Covert to List
    template_name = 'origin.html'  # Template Name
    context_object_name = 'origin'  # Change default name of objectList
    ordering = ['-id']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Origin List"
        context["nav_bar"] = "origin_list"
        context['origin'] = self.model.objects.all().order_by('-id')
        return context


def add_new_origin(request):
    print("called")
    template_name = 'add_origin.html'

    if request.method == 'GET':
        print("called GET")
        origin_form = OriginCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        origin_form = OriginCreateForm(request.POST)

        if origin_form.is_valid():
            obj = origin_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Origin Country Added Successfully!')
            return redirect('all-origins')

        else:
            print("Not Valid Create Form")
            print(origin_form.errors)

    return render(request, template_name, {
        'origin_form': origin_form,
        'title': 'Add New Origin',
        'nav_bar': 'add_new_origin',
    })


class OriginUpdateView(SuccessMessageMixin, UpdateView):
    model = Origin
    form_class = OriginCreateForm
    success_url = reverse_lazy('all-origins')
    template_name = 'update_origin.html'
    success_message = "Origin Country was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Origin Country Information"
        context["nav_bar"] = "origin_list"
        return context


def origin_delete(request, id):
    if request.method == 'GET':
        instance = Origin.objects.get(id=id)
        Origin.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-origins')


class AllDestinationListView(ListView):
    model = Destination  # Model I want to Covert to List
    template_name = 'destination.html'  # Template Name
    context_object_name = 'destination'  # Change default name of objectList
    ordering = ['-id']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Destination List"
        context["nav_bar"] = "destination_list"
        context['destination'] = self.model.objects.all().order_by('-id')
        return context


def add_new_destination(request):
    print("called")
    template_name = 'add_destination.html'

    if request.method == 'GET':
        print("called GET")
        destination_form = DestinationCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        destination_form = DestinationCreateForm(request.POST)

        if destination_form.is_valid():
            obj = destination_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Destination Country Added Successfully!')
            return redirect('all-destinations')

        else:
            print("Not Valid Create Form")
            print(destination_form.errors)

    return render(request, template_name, {
        'destination_form': destination_form,
        'title': 'Add New Destination',
        'nav_bar': 'add_new_destination',
    })


class DestinationUpdateView(SuccessMessageMixin, UpdateView):
    model = Destination
    form_class = DestinationCreateForm
    success_url = reverse_lazy('all-destinations')
    template_name = 'update_destination.html'
    success_message = "Destination Country was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Destination Country Information"
        context["nav_bar"] = "destination_list"
        return context

class AllExtraListView(ListView):
    model = Shipper  # Model I want to Covert to List
    template_name = 'extra.html'  # Template Name
    context_object_name = 'shipper'  # Change default name of objectList
    ordering = ['-id']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Extra List"
        context["nav_bar"] = "extra_list"
        context['shipper'] = self.model.objects.all().order_by('-id')
        return context


def destination_delete(request, id):
    if request.method == 'GET':
        instance = Destination.objects.get(id=id)
        Destination.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-destinations')

def sales_delete(request, id):
    if request.method == 'GET':
        instance = Shipper.objects.get(id=id)
        Shipper.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-extras')








