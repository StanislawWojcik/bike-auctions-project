from django.contrib import admin
from .models import Auction, Order

admin.site.register(Auction)
admin.site.register(Order)