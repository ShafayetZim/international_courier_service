from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from django.views.generic import ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .utils import render_to_pdf
from .forms import *
from .models import *
from django.urls import reverse
# Create your views here.


class AllShipperListView(ListView):
    model = Sender  # Model I want to Covert to List
    template_name = 'transaction/shipper.html'  # Template Name
    context_object_name = 'shipper'  # Change default name of objectList
    ordering = ['-shipper_code']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shipper List"
        context["nav_bar"] = "shipper_list"
        context['shipper'] = self.model.objects.all().order_by('-shipper_code')
        return context


def new_shipper(request):
    print("called")
    template_name = 'transaction/new_shipper.html'

    if request.method == 'GET':
        print("called GET")
        shipper_form = ShipperCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        shipper_form = ShipperCreateForm(request.POST)

        if shipper_form.is_valid():
            obj = shipper_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Shipper Added Successfully!')
            return redirect('all-shippers')

        else:
            print("Not Valid Create Form")
            print(shipper_form.errors)

    return render(request, template_name, {
        'shipper_form': shipper_form,
        'title': 'New Shipper',
        'nav_bar': 'new_shipper',
    })


class ShipperUpdateView(SuccessMessageMixin, UpdateView):
    model = Sender
    form_class = ShipperUpdateForm
    success_url = reverse_lazy('all-shippers')
    template_name = 'transaction/update_shipper.html'
    success_message = "Shipper was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Shipper Information"
        context["nav_bar"] = "shipper_list"
        return context


def shipper_delete(request, shipper_code):
    if request.method == 'GET':
        instance = Sender.objects.get(shipper_code=shipper_code)
        Sender.objects.filter(shipper_code=instance.shipper_code).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-shippers')


class ShipperDetailView(DetailView):
    model = Sender
    template_name = 'transaction/shipper_detail.html'
    context_object_name = 'ship'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shipper Information"
        context["nav_bar"] = "shipper_list"
        return context


class AllReceiverListView(ListView):
    model = Receiver  # Model I want to Covert to List
    template_name = 'transaction/receiver.html'  # Template Name
    context_object_name = 'receiver'  # Change default name of objectList
    ordering = ['-receiver_code']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Receiver List"
        context["nav_bar"] = "receiver_list"
        context['receiver'] = self.model.objects.all().order_by('-receiver_code')
        return context


def new_receiver(request):
    print("called")
    template_name = 'transaction/new_receiver.html'

    if request.method == 'GET':
        print("called GET")
        receiver_form = ReceiverCreateForm(request.GET or None)

    elif request.method == 'POST':
        print("called POST")
        print(request.POST)
        receiver_form = ReceiverCreateForm(request.POST)

        if receiver_form.is_valid():
            obj = receiver_form.save(commit=False)
            obj.author = request.user
            obj.is_active = True
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'New Receiver Added Successfully!')
            return redirect('all-receivers')

        else:
            print("Not Valid Create Form")
            print(receiver_form.errors)

    return render(request, template_name, {
        'receiver_form': receiver_form,
        'title': 'New Receiver',
        'nav_bar': 'new_receiver',
    })


class ReceiverUpdateView(SuccessMessageMixin, UpdateView):
    model = Receiver
    form_class = ReceiverUpdateForm
    success_url = reverse_lazy('all-receivers')
    template_name = 'transaction/update_receiver.html'
    success_message = "Receiver was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Receiver Information"
        context["nav_bar"] = "receiver_list"
        return context


class ReceiverDetailView(DetailView):
    model = Receiver
    template_name = 'transaction/receiver_detail.html'
    context_object_name = 'receive'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Receiver Information"
        context["nav_bar"] = "receiver_list"
        return context


def receiver_delete(request, receiver_code):
    if request.method == 'GET':
        instance = Receiver.objects.get(receiver_code=receiver_code)
        Receiver.objects.filter(receiver_code=instance.receiver_code).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-receivers')


class AllShipmentListView(ListView):
    model = Transaction  # Model I want to Convert to List
    template_name = 'transaction/shipment.html'  # Template Name
    context_object_name = 'shipment'  # Change default name of objectList
    ordering = ['-shipment_no']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shipment List"
        context["nav_bar"] = "shipment_list"
        context['shipment'] = self.model.objects.all().order_by('-shipment_date','-shipment_no')
        return context


def new_shipment(request):
    template_name = 'transaction/add_shipment.html'

    if request.method == 'GET':
        print("GET called")
        sales_form = ShipmentCreateForm(None)

    elif request.method == 'POST':
        print("Post called")
        sales_form = ShipmentCreateForm(request.POST)

        if 'preview' in request.POST:
            sales_form = ShipmentCreateForm(request.POST)
        if 'submit' in request.POST:

            if sales_form.is_valid():
                sales_parent = sales_form.save(commit=False)
                sales_parent.author = request.user
                sales_parent.is_active = True
                sales_parent.save()

                messages.add_message(request, messages.SUCCESS, 'New Shipment Entry Successful')
                # return redirect('all-shipments')

                def get_absolute_url(self):
                    return reverse('shipment-edit', kwargs={'pk': self.pk})

            else:
                print("Not Valid Create Form")
                print(sales_form.errors)

    return render(request, template_name, {
        'sales_form': sales_form,
        'title': 'New Shipment',
        'nav_bar': 'new_shipment',
    })


def shipment_edit(request, shipment_no):
    template_name = 'transaction/update_shipment.html'

    if request.method == 'GET':
        print("GET called")
        parent = get_object_or_404(Transaction, shipment_no=shipment_no)
        sales_form = ShipmentUpdateForm(instance=parent)

    elif request.method == 'POST':
        print("Post called")
        parent = get_object_or_404(Transaction, shipment_no=shipment_no)
        sales_form = ShipmentUpdateForm(request.POST, instance=parent)

        if sales_form.is_valid():
            sales_parent = sales_form.save(commit=False)
            sales_parent.author = request.user
            sales_parent.is_active = True
            sales_parent.save()

            messages.add_message(request, messages.SUCCESS, 'Shipment Update Successful')
            return redirect('all-shipments')

        else:
            print("Not Valid Create Form")
            print(sales_form.errors)

    return render(request, template_name, {
        'sales_form': sales_form,
        'title': 'New Sales',
        'nav_bar': 'new_sales',
    })


class ShippingStatus(SuccessMessageMixin, UpdateView):
    model = Transaction
    form_class = ShippingStatusForm
    success_url = reverse_lazy('all-shipments')
    template_name = 'transaction/shipping_status.html'
    success_message = "Shipping was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Shipping Status"
        context["nav_bar"] = "shipment_list"
        return context


class ShipmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Transaction
    form_class = ShipmentUpdateForm
    success_url = reverse_lazy('all-shipments')
    template_name = 'transaction/update_shipment.html'
    success_message = "Shipment was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Shipment Information"
        context["nav_bar"] = "shipment_list"
        return context


class ShipmentDetailView(DetailView):
    model = Transaction
    template_name = 'transaction/shipment_detail.html'
    context_object_name = 'shipment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shipment Information"
        context["nav_bar"] = "shipment_list"
        return context


class DetailView(DetailView):
    model = Transaction
    template_name = 'details.html'
    context_object_name = 'sales_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Shipment Information"
        context["nav_bar"] = "shipment_list"
        return context


def shipment_delete(request, shipment_no):
    if request.method == 'GET':
        instance = Transaction.objects.get(shipment_no=shipment_no)
        Transaction.objects.filter(shipment_no=instance.shipment_no).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-shipments')


def shipper_info(request):
    print("shipper_info called")
    shipper_code = request.GET.get('shipper_code', None)
    shipper = Sender.objects.get(shipper_code=shipper_code)
    data = {
        'street': shipper.shipper_address,
        'mobile': shipper.mobile,
        'city': shipper.city,
        'state': shipper.state,
        'zip': shipper.zip,
        'telephone': shipper.telephone,
        'name': shipper.shipper_name,
        'nid': shipper.nid,
    }
    print(data)
    return JsonResponse(data, status=200)


def receiver_info(request):
    print("receiver_info called")
    receiver_code = request.GET.get('receiver_code', None)
    receiver = Receiver.objects.get(receiver_code=receiver_code)
    data = {
        'address': receiver.receiver_address,
        'phone': receiver.mobile,
        'town': receiver.city,
        'states': receiver.state,
        'zipcode': receiver.zip,
        'tphone': receiver.telephone,
        'recipient': receiver.receiver_name,
        'passport': receiver.nid,
    }
    print(data)
    return JsonResponse(data, status=200)


def print_invoice(request, shipment_no):
    print(shipment_no)
    shipment = Transaction.objects.get(shipment_no=shipment_no)

    # print('%d in words is: %s' % (total_amount, getWords(total_amount)))

    context = {
        'title': "Shipment",
        'nav_bar': "shipment_list",
        'shipment': shipment,
    }
    pdf = render_to_pdf('transaction/invoice.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


def airway_bill(request, shipment_no):
    print(shipment_no)
    shipment = Transaction.objects.get(shipment_no=shipment_no)

    # print('%d in words is: %s' % (total_amount, getWords(total_amount)))

    context = {
        'title': "Shipment",
        'nav_bar': "shipment_list",
        'shipment': shipment,
    }
    pdf = render_to_pdf('transaction/airway_bill.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


def money_receipt(request, shipment_no):
    print(shipment_no)
    shipment = Transaction.objects.get(shipment_no=shipment_no)

    # print('%d in words is: %s' % (total_amount, getWords(total_amount)))

    context = {
        'title': "Shipment",
        'nav_bar': "shipment_list",
        'shipment': shipment,
    }
    pdf = render_to_pdf('transaction/money_receipt.html', context)
    return HttpResponse(pdf, content_type='application/pdf')