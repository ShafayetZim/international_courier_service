from django import forms
from django.forms import modelformset_factory

from sales.models import SalesParent, SalesChild, Customers, Shipper


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = (
            'customer_code', 'customer_name', 'customer_address', 'phone', 'email', 'bin_no',)
        # reference link below
        # https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#custom-fields-placement-with-crispy-forms
        widgets = {
            'customer_code': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'bin_no': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ShipperCreateForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = (
            'shipper_code', 'shipper_company', 'shipper_address', 'city', 'state', 'zip', 'shipper_name', 'mobile', 'telephone',)
        # reference link below
        # https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html#custom-fields-placement-with-crispy-forms
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

        }


class SalesCreateForm(forms.ModelForm):
    class Meta:
        model = SalesParent
        fields = (
            'customer', 'address', 'phone', 'shipper', 'street', 'city', 'state', 'zip', 'shipper_name', 'mobile', 'telephone', 'order_date', 'quantity',
            'total_amount', 'paid_amount', 'due_amount',)
        widgets = {
            'customer': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_customer'}),
            
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper': forms.Select(
                attrs={'required': True, 'class': 'form-control', 'value': '', 'id': 'id_shipper'}),
            
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'shipper_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly', 'value': '', 'id': 'sales_total_qty'}),
            'total_amount': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly', 'value': '', 'id': 'sales_total_amount'}),
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control', 'value': '', 'id': 'sales_paid_amount'}),
            'due_amount': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': 'readonly', 'value': '', 'id': 'sales_due_amount'}),
            'order_date': forms.DateTimeInput(format='%Y-%m-%d',
                                              attrs={'required': True, 'class': 'form-control', 'type': 'date', }),
        }
        labels = {
            'customer': 'Customer Name',
            'address': 'Address',
            'phone': 'Phone',
            'shipper': 'Shipper Company',
            'street': 'Street',
            'mobile': 'Mobile',
            'order_date': 'Order Date',
            'quantity': 'Total Qty',
            'total_amount': 'Total Amount',
            'paid_amount': 'Paid Amount',
            'due_amount': 'Due Amount',
        }


packing_type = [('Box', 'Box'), ('Carton', 'Carton'), ('Bundle', 'Bundle'), ('Bag', 'Bag'), ('Pack', 'Pack'),
                ('Pallet', 'Pallet'), ('Roll', 'Roll'), ('Set', 'Set'), ('Jar', 'Jar'), ('Drum', 'Drum'),
                ('Bucket', 'Bucket')]


class SalesChildFormCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['quantity'].widget.attrs.update(
            {'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['price'].widget.attrs.update(
            {'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
        self.fields['amount'].widget.attrs.update(
            {'class': 'textinput form-control setprice amount', 'min': '0', 'required': 'true',
             'readonly': 'readonly', })
        self.fields['extra_field'].widget.attrs.update(
            {'class': 'textinput form-control setprice extra_field', 'min': '0', 'required': 'true',
             'readonly': 'readonly', })

    class Meta:
        model = SalesChild
        fields = (
            'quantity', 'price', 'amount', 'packing_qty', 'packing_unit', 'extra_field')


SalesChildFormset = modelformset_factory(
    SalesChild,
    form=SalesChildFormCreateForm,
    extra=1,
    widgets={
        'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        'price': forms.NumberInput(attrs={'class': 'form-control'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'packing_qty': forms.NumberInput(attrs={'required': 'true', 'class': 'form-control'}),
        'packing_unit': forms.Select(choices=packing_type, attrs={'class': 'form-control'}),
        'extra_field': forms.NumberInput(attrs={'class': 'form-control', }),
    },
)
