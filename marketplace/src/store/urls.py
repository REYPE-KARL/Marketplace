from django.urls import path

from store.views import index, product_detail, add_to_cart, cart, delete_cart, order_cart

urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('cart/order', order_cart, name='order-cart'),
    path('cart/delete', delete_cart, name='delete-cart'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add-to-cart'),
]