from .models import Courier, Origin, Destination, Shipper, Receiver
from django import forms

class CourierCreateForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = (
            'name', 'address', 'mobile', 'email', 'remark')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),

        }


class OriginCreateForm(forms.ModelForm):
    class Meta:
        model = Origin
        fields = (
            'name', 'code', 'remark')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),

        }


class DestinationCreateForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = (
            'name', 'code', 'remark')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ShipperCreateForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = (
            'company', 'address', 'city', 'state', 'zip', 'name', 'telephone', 'mobile',)
        
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ReceiverCreateForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = (
            'company', 'address', 'city', 'state', 'zip', 'name', 'telephone', 'mobile',)
        
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),

        }