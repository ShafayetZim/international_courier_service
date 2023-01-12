from django.db import models
from dataset.models import *
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    # sender
    sender_attention = models.CharField(max_length=100)
    sender_company = models.CharField(max_length=100, blank=True, null=True)
    sender_address = models.CharField(max_length=100, blank=True, null=True)
    sender_city = models.CharField(max_length=100, blank=True, null=True)
    sender_zip = models.CharField(max_length=100, blank=True, null=True)
    sender_country = models.ForeignKey(Origin, on_delete=models.DO_NOTHING, )
    sender_phone = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=100, blank=True, null=True)
    sender_nid = models.CharField(max_length=100, blank=True, null=True)
    # receiver
    receiver_attention = models.CharField(max_length=100)
    receiver_company = models.CharField(max_length=100, blank=True, null=True)
    receiver_address = models.CharField(max_length=100)
    receiver_city = models.CharField(max_length=100)
    receiver_zip = models.CharField(max_length=100)
    receiver_country = models.ForeignKey(Destination, on_delete=models.DO_NOTHING, )
    receiver_phone = models.CharField(max_length=100)
    receiver_email = models.CharField(max_length=100, blank=True, null=True)
    receiver_nid = models.CharField(max_length=100, blank=True, null=True)
    # shipping info
    PAYMENT_CHOICES = (
        ('Prepaid', 'Prepaid'),
        ('Collect', 'Collect'),
    )
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='Prepaid')
    ship_ref = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    piece = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    product_value = models.CharField(max_length=100, blank=True, null=True)
    ITEM_CHOICES = (
        ('Sample', 'Sample'),
        ('Document', 'Document'),
        ('Envelope', 'Envelope'),
    )
    item = models.CharField(max_length=20, choices=ITEM_CHOICES, default='Sample')
    remarks = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    length = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, )

    def __str__(self):
        return self.sender_attention


class Office(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
