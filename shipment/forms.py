from dataclasses import fields
from django import forms
from .models import *

class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = (
            'shipment_no', 'shipper_account', 'shipper_company', 'shipper_address',
            'shipper_city', 'shipper_state', 'shipper_zip', 'shipper_name',
            'shipper_telephone', 'shipper_mobile', 'origin_country', 'receiver_company',
            'receiver_address', 'receiver_city', 'receiver_state', 'receiver_zip',
            'receiver_name', 'receiver_telephone', 'receiver_mobile', 'destination_country',
            'ref_no', 'courier', 'awb_no', 'piece', 'weight', 'content', 'remark',
            'height', 'width', 'length', 'pickup_by', 'pickup_date', 'currency',
            'prepaid_amount', 'collect_amount', 'third_party_amount', 'cheque_no',
            'account_no', 
        )
        widgets = {
            'shipment_no': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_account': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_company': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_shipper'}
            ),
            'shipper_address': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_city': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_state': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_name': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'origin_country': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'receiver_company': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_receiver'}
            ),
            'receiver_address': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_city': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_state': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'destination_country': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'ref_no': forms.TextInput(attrs={'class': 'form-control'}),
            'courier': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'awb_no': forms.TextInput(attrs={'class': 'form-control'}),
            'piece': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'remark': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'width': forms.TextInput(attrs={'class': 'form-control'}),
            'length': forms.TextInput(attrs={'class': 'form-control'}),
            'pickup_by': forms.TextInput(attrs={'class': 'form-control'}),
            'pickup_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'currency': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'prepaid_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'collect_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'third_party_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'cheque_no': forms.TextInput(attrs={'class': 'form-control'}),
            'account_no': forms.TextInput(attrs={'class': 'form-control'}),
        }