from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from dataset.models import Shipper
from shipment.forms import ShipmentCreateForm

from shipment.models import Shipment
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

def tpc_dashboard(request):
    context = {'title': 'Shipment',
               'nav_bar': 'dashboard',
               }
    return render(request, 'dashboard.html', context)


# class ShipmentListView(ListView, ):
#     model = Shipment  # Model I want to Covert to List
#     template_name = 'shipment.html'  # Template Name
#     context_object_name = 'shipment'  # Change default name of objectList
#     ordering = ['-shipment_no', '-created_at']  # Ordering post LIFO
#     paginate_by = 20  # number of page I want to show in single page

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Shipment List"
#         context["nav_bar"] = "shipment_list"
#         context['shipment'] = self.model.objects.all()
#         return context


# def new_shipment(request):
#     template_name = 'add_shipment.html'

#     if request.method == 'GET':
#         print("GET called")
#         shipment_form = ShipmentCreateForm(request.GET or None)

#     elif request.method == 'POST':
#         print("Post called")
#         shipment_form = ShipmentCreateForm(request.POST)

#         if shipment_form.is_valid():
#             obj = shipment_form.save(commit=False)
#             obj.author = request.user
#             obj.is_active = True
#             obj.save()

#             messages.add_message(request, messages.SUCCESS, 'New Shipment Entry Successful')
#             return redirect('shipment-list')

#         else:
#             print("Not Valid Create Form")
#             print(shipment_form.errors)

#     return render(request, template_name, {
#         'shipment_form': shipment_form,
#         'title': 'New Shipment',
#         'nav_bar': 'new_shipment',
#     })


# def shipper_info(request):
#     print("shipper_info called")
#     shipper_code = request.GET.get('pk', None)
#     shipper = Shipper.objects.get(pk=shipper_code)
#     data = {
#         'address': shipper.address,
#         'mobile': shipper.mobile,
#     }
#     # print(data)
#     return JsonResponse(data, status=200)
