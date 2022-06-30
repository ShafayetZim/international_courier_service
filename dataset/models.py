from ctypes import addressof
from inspect import modulesbyfile
from unicodedata import name
from django.db import models

# Create your models here.


class Courier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True) 
    email = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Origin(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=200, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=200, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Shipper(models.Model):
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=20)
    name = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.company


class Receiver(models.Model):
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=20)
    name = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.company



