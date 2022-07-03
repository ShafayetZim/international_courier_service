from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from dataset.models import Shipper
from shipment.forms import UserRegisterForm, UpdateUser

from shipment.models import Shipment
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def tpc_dashboard(request):
    context = {'title': 'Shipment',
               'nav_bar': 'dashboard',
               }
    return render(request, 'dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'Account has been created! S/He Can login now.')
            return redirect('all-users')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form,'title': 'New User','nav_bar': 'new_user',})


class AllUserListView(ListView):
    model = User  # Model I want to Covert to List
    template_name = 'user_list.html'  # Template Name
    context_object_name = 'user'  # Change default name of objectList
    ordering = ['-id']  # Ordering post LIFO
    paginate_by = 20  # number of page I want to show in single page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User List"
        context["nav_bar"] = "user_list"
        context['user'] = self.model.objects.filter(is_superuser = False).all().order_by('-id')
        return context


def user_delete(request, id):
    if request.method == 'GET':
        instance = User.objects.get(id=id)
        User.objects.filter(id=instance.id).delete()
        instance.delete()
        messages.add_message(request, messages.WARNING, 'Delete Success')
        return redirect('all-users')


class UserUpdateView(UpdateView):
    model = User
    form_class = UpdateUser
    success_url = reverse_lazy('all-users')
    template_name = 'update_user.html'
    success_message = "User was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User Information"
        context["nav_bar"] = "user_list"
        return context