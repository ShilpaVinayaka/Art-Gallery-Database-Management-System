from django.contrib import admin
from .models import Gallery, Artist, Artwork, Exhibition, Instock,Order, Customer, OrderItem, ShippingAddress, Customerdetails

 #Register your models here.

admin.site.register(Gallery),
admin.site.register(Artist),
admin.site.register(Artwork),
admin.site.register(Exhibition),
admin.site.register(Instock),
admin.site.register(Customer),
admin.site.register(Customerdetails),
admin.site.register(Order),
admin.site.register(OrderItem),
admin.site.register(ShippingAddress)


