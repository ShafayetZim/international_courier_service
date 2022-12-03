from django import forms
from .models import *


class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'sender_attention', 'sender_company', 'sender_address', 'sender_city', 'sender_zip', 'sender_country',
            'sender_phone', 'sender_email', 'receiver_attention', 'receiver_company', 'receiver_address',
            'receiver_city', 'receiver_zip', 'receiver_country', 'receiver_phone', 'receiver_email', 'payment',
            'ship_ref', 'weight', 'piece', 'product_value', 'item', 'remarks', 'description', 'length',
            'height', 'width', 'sender_nid', 'receiver_nid',
        )
        widgets = {
            'sender_attention': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_company': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_address': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_city': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_country': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'sender_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_email': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_attention': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_company': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_address': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_city': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_country': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'receiver_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_email': forms.TextInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'ship_ref': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'piece': forms.TextInput(attrs={'class': 'form-control'}),
            'product_value': forms.TextInput(attrs={'class': 'form-control'}),
            'item': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'length': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'width': forms.TextInput(attrs={'class': 'form-control'}),
            'sender_nid': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_nid': forms.TextInput(attrs={'class': 'form-control'}),
        }