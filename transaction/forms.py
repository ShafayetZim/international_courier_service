from django import forms
from .models import *


class ShipperCreateForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = (
            'shipper_code', 'shipper_company', 'shipper_address', 'city', 'state', 'zip', 'shipper_name', 'mobile', 'telephone', 'nid',)
        
        widgets = {
            'shipper_code': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'shipper_company': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'nid': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ShipperUpdateForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = (
            'shipper_company', 'shipper_address', 'city', 'state', 'zip', 'shipper_name', 'mobile',
            'telephone', 'nid',)

        widgets = {
            'shipper_company': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'nid': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReceiverCreateForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = (
            'receiver_code', 'receiver_company', 'receiver_address', 'city', 'state', 'zip', 'receiver_name', 'mobile', 'telephone', 'nid',)
        
        widgets = {
            'receiver_code': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'receiver_company': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'nid': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReceiverUpdateForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = (
            'receiver_company', 'receiver_address', 'city', 'state', 'zip', 'receiver_name', 'mobile',
            'telephone', 'nid',)

        widgets = {
            'receiver_code': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'receiver_company': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'nid': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ShipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = (
            'shipment_date', 'shipper_account', 'shipper', 'shipper_address', 'shipper_city', 'shipper_state', 'shipper_zip', 'shipper_name', 'shipper_mobile', 'shipper_telephone',
            'origin_country', 'destination_country', 'receiver', 'receiver_address', 'receiver_city', 'receiver_state', 'receiver_zip', 'receiver_name', 'receiver_mobile', 'receiver_telephone',
            'ref_no', 'courier', 'awb_no', 'piece', 'weight', 'content', 'remark', 'height', 'width', 'length', 'pickup_by', 'pickup_date', 'currency', 'prepaid_amount', 'collect_amount',
            'third_party_amount', 'cheque_no', 'account_no', 'shipper_nid', 'receiver_nid',
            )
        widgets = {
            'shipment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date',}),
            'shipper_account': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_shipper'}),
            
            'shipper_address': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_city': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_state': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_name': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_nid': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_receiver'}),
            
            'receiver_address': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_city': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_state': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_nid': forms.TextInput(attrs={'class': 'form-control'}),
            'origin_country': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
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
            'pickup_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'currency': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'prepaid_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'collect_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'third_party_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'cheque_no': forms.TextInput(attrs={'class': 'form-control'}),
            'account_no': forms.TextInput(attrs={'class': 'form-control'}),
            
        }


class ShipmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = (
            'status', 'shipper_account', 'shipper', 'shipper_address', 'shipper_city', 'shipper_state',
            'shipper_zip', 'shipper_name', 'shipper_mobile', 'shipper_telephone',
            'origin_country', 'destination_country', 'receiver', 'receiver_address', 'receiver_city', 'receiver_state',
            'receiver_zip', 'receiver_name', 'receiver_mobile', 'receiver_telephone',
            'ref_no', 'courier', 'awb_no', 'piece', 'weight', 'content', 'remark', 'height', 'width', 'length',
            'pickup_by', 'pickup_date', 'currency', 'prepaid_amount', 'collect_amount',
            'third_party_amount', 'cheque_no', 'account_no', 'shipper_nid', 'receiver_nid',
        )
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control', }),
            'shipper_account': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_shipper'}),

            'shipper_address': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_city': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_state': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_name': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_nid': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_receiver'}),

            'receiver_address': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_city': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_state': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_zip': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'receiver_nid': forms.TextInput(attrs={'class': 'form-control'}),
            'origin_country': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
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
            'pickup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'currency': forms.Select(
                attrs={'required': True, 'class': 'form-control'}
            ),
            'prepaid_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'collect_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'third_party_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'cheque_no': forms.TextInput(attrs={'class': 'form-control'}),
            'account_no': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ShippingStatusForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('status', )

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control', 'required': True}),

        }