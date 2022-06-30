from django.contrib import admin
from .models import Courier, Origin, Destination, Shipper, Receiver

# Register your models here.
admin.site.register(Courier)
admin.site.register(Origin)
admin.site.register(Destination)
admin.site.register(Shipper)
admin.site.register(Receiver)