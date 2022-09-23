from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime
from dataset.models import *
# Create your models here.


def shipment_no_generate():
    today_date = datetime.date.today()

    # GET Current Year
    current_year = today_date.strftime('%Y')
    prefix = "TPC-" + current_year + "-"

    # For the very first time invoice_number is DD-MM-YY-0001
    next_shipment_no = '00001'

    # Get Last invoice Start With TPC-
    last_shipment_no = Shipment.objects.filter(shipment_no__startswith=prefix).order_by('shipment_no').last()

    if last_shipment_no:
        # Cut 5 digit from the Right and converted to int (STC-YYYY-:xxxx)
        last_shipment_four_digit = int(last_shipment_no.invoice_no[-5:])

        # Increment one with last five digit
        next_shipment_no = '{0:05d}'.format(last_shipment_four_digit + 1)

    # Return custom invoice number
    return prefix + next_shipment_no


class Shipment(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    shipment_no = models.CharField(max_length=100, primary_key=True, default=shipment_no_generate)
    shipper_account = models.CharField(max_length=100)
    shipper_company = models.ForeignKey(Shipper, on_delete=models.DO_NOTHING, )
    shipper_address = models.CharField(max_length=200)
    shipper_city = models.CharField(max_length=200)
    shipper_state = models.CharField(max_length=200, blank=True, null=True)
    shipper_zip = models.CharField(max_length=20)
    shipper_name = models.CharField(max_length=200, blank=True, null=True)
    shipper_telephone = models.CharField(max_length=20, blank=True, null=True)
    shipper_mobile = models.CharField(max_length=200, blank=True, null=True)
    origin_country = models.ForeignKey(Origin, on_delete=models.DO_NOTHING, )
    receiver_company = models.ForeignKey(Receiver, on_delete=models.DO_NOTHING, )
    receiver_address = models.CharField(max_length=200)
    receiver_city = models.CharField(max_length=200)
    receiver_state = models.CharField(max_length=200, blank=True, null=True)
    receiver_zip = models.CharField(max_length=20)
    receiver_name = models.CharField(max_length=200, blank=True, null=True)
    receiver_telephone = models.CharField(max_length=20, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=200, blank=True, null=True)
    destination_country = models.ForeignKey(Destination, on_delete=models.DO_NOTHING, )
    ref_no = models.CharField(max_length=200, blank=True, null=True)
    courier = models.ForeignKey(Courier, on_delete=models.DO_NOTHING, )
    awb_no = models.CharField(max_length=200, blank=True, null=True)
    piece = models.IntegerField(blank=True, null=True, default=1)
    weight = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    CONTENT_CHOICES = (
        ('Sample', 'Sample'),
        ('Document', 'Document'),
        ('Envelope', 'Envelope'),
    )
    content = models.CharField(max_length=20, choices=CONTENT_CHOICES, default='Sample')
    remark = models.CharField(max_length=200, blank=True, null=True)
    height = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    length = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    pickup_by = models.CharField(max_length=200, blank=True, null=True)
    pickup_date = models.DateField(blank=True, null=True)
    CURRENCY_CHOICES = (
        ('BDT', 'BDT'),
        ('USD', 'USD'),
        ('EURO', 'EURO'),
    )
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default='BDT')
    prepaid_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    collect_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    third_party_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    cheque_no = models.CharField(max_length=200, blank=True, null=True)
    account_no = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, )

    def __str__(self):
        return self.shipment_no

