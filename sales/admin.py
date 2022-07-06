from django.contrib import admin

from sales.models import SalesParent, SalesChild, Customers, Shipper

admin.site.register(SalesParent)
admin.site.register(SalesChild)
admin.site.register(Customers)
admin.site.register(Shipper)