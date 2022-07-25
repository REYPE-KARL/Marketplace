from django.contrib import admin
from store.models import Product, Order, Cart


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('user', 'product',)
    list_display = ('user', 'product', 'quantity', 'ordered', 'ordered_date',)
    list_filter = ('user', 'product',)
    ordering = ('user',)


class CartAdmin(admin.ModelAdmin):
    search_fields = ('user', 'orders',)
    list_display = ('user',)
    list_filter = ('user', 'orders',)
    ordering = ('user',)


admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
