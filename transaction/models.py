from django.contrib.auth.models import User
from django.db import models
import datetime
from dataset.models import *
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.


def shipper_code():
    prifix = "S-"
    next_number = '00001'
    last_number = Sender.objects.filter(shipper_code__startswith=prifix).order_by('shipper_code').last()
    if last_number:
        last_code = int(last_number.shipper_code[4:])
        next_number = '{0:05d}'.format(last_code + 1)
    return prifix + next_number


class Sender(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    shipper_code = models.CharField(max_length=20, primary_key=True, default=shipper_code)
    shipper_company = models.CharField(max_length=100)
    shipper_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100)
    shipper_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    nid = models.CharField(max_length=50, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.shipper_company


def receiver_code():
    prifix = "R-"
    next_number = '00001'
    last_number = Receiver.objects.filter(receiver_code__startswith=prifix).order_by('receiver_code').last()
    if last_number:
        last_code = int(last_number.receiver_code[4:])
        next_number = '{0:05d}'.format(last_code + 1)
    return prifix + next_number


class Receiver(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    receiver_code = models.CharField(max_length=20, primary_key=True, default=receiver_code)
    receiver_company = models.CharField(max_length=100)
    receiver_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    nid = models.CharField(max_length=50, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.receiver_company


def shipment_no_generate():
    today_date = datetime.date.today()

    # GET Current Year
    current_year = today_date.strftime('%d%m%y')
    prefix = "" + current_year

    # For the very first time shipment_number is DD-MM-YY-0001
    next_shipment_no = '0001'

    # Get Last Shipment Start With TPC-
    last_shipment_no = Transaction.objects.filter(shipment_no__startswith=prefix).order_by('shipment_no').last()

    if last_shipment_no:
        # Cut 4 digit from the Right and converted to int (STC-YYYY-:xxxx)
        last_shipment_four_digit = int(last_shipment_no.shipment_no[-4:])

        # Increment one with last four digit
        next_shipment_no = '{0:04d}'.format(last_shipment_four_digit + 1)

    # Return custom shipment number
    return prefix + next_shipment_no


class Transaction(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    shipment_date = models.DateTimeField(blank=True, null=True, )
    shipment_no = models.CharField(max_length=100, primary_key=True, default=shipment_no_generate)
    shipper_account = models.CharField(max_length=100)
    shipper = models.ForeignKey(Sender, on_delete=models.DO_NOTHING, )
    shipper_address = models.CharField(max_length=200,)
    shipper_city = models.CharField(max_length=200,)
    shipper_state = models.CharField(max_length=200, blank=True, null=True)
    shipper_zip = models.CharField(max_length=200,)
    shipper_name = models.CharField(max_length=200, blank=True, null=True)
    shipper_mobile = models.CharField(max_length=20, blank=True, null=True)
    shipper_telephone = models.CharField(max_length=20, blank=True, null=True)
    shipper_nid = models.CharField(max_length=50, blank=True, null=True)
    origin_country = models.ForeignKey(Origin, on_delete=models.DO_NOTHING, )
    receiver = models.ForeignKey(Receiver, on_delete=models.DO_NOTHING, )
    receiver_address = models.CharField(max_length=200,)
    receiver_city = models.CharField(max_length=200,)
    receiver_state = models.CharField(max_length=200, blank=True, null=True)
    receiver_zip = models.CharField(max_length=200,)
    receiver_name = models.CharField(max_length=200, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=20, blank=True, null=True)
    receiver_telephone = models.CharField(max_length=20, blank=True, null=True)
    receiver_nid = models.CharField(max_length=50, blank=True, null=True)
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
    barcode = models.ImageField(upload_to='barcode', blank=True, null=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Shipped', 'Shipped'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.shipment_no

    # barcode generator
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('code128')
        ean = EAN(f'{self.shipment_no}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)
