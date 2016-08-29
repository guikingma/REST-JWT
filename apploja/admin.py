from django.contrib import admin
from models import Order
from models import Product


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'description',
    )
    list_filter = (
        'description',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'price', 'order'
    )
    list_filter = (
        'name',
    )

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
